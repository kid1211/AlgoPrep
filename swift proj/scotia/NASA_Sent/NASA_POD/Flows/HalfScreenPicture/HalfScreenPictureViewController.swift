//
//  ViewController.swift
//  NASA_POD
//
//  Created by Xujie Zheng on 2020-08-28.
//  Copyright © 2020 Xujie Zheng. All rights reserved.
//

import UIKit
import Combine

class HalfScreenPictureViewController: UIViewController, UIViewControllerTransitioningDelegate {
    // MARK: - IBOutlet

    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var imageTitle: UILabel!

    // MARK: - Properties

    private var viewModel = HalfScreenPictureViewModel()
    private var isFetchingSubscriber: AnyCancellable?
    private var viewDataSubscriber: AnyCancellable?
    private var errorMessageSubscriber: AnyCancellable?

    // MARK: - Life Cycle

    deinit {
        isFetchingSubscriber?.cancel()
        viewDataSubscriber?.cancel()
        errorMessageSubscriber?.cancel()
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        setupView()

        subscribeToIsFetching()
        subscribeViewData()
        subscribeErrorMessage()

        viewModel.startFetching()
    }

    // MARK: - Helpers

    override var shouldAutorotate: Bool {
//        if let imageView = imageView, let image = imageView.image {
//            return image.size.width > image.size.height
//        }
        return false
    }

    private func setupView() {
        let tapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(imageTapped(tapGestureRecognizer:)))
        imageView.isUserInteractionEnabled = true
        imageView.addGestureRecognizer(tapGestureRecognizer)
    }

    @objc func imageTapped(tapGestureRecognizer: UITapGestureRecognizer) {
        presentFullScreenPictureViewController()
    }

    private func presentFullScreenPictureViewController() {
        let storyboard = UIStoryboard(name: "Main", bundle: nil)
        guard
            let viewController = storyboard.instantiateViewController(withIdentifier: "FullScreenViewController") as? FullScreenPictureViewController
            else { return }
        // .fullScreen won't work due to the black flicker
        viewController.modalPresentationStyle = .overCurrentContext
        viewController.transitioningDelegate = self
        viewController.viewData = viewModel.viewData // Rotate Data only not the entire screen

        if shouldAutorotate {
            viewController.beforeDismiss = rotateToPortrait
            rotateToLandscape()
        }
        present(viewController, animated: true, completion: nil)
    }
}

extension HalfScreenPictureViewController {
    // MARK: - Animation

    func animationController(
        forPresented presented: UIViewController,
        presenting: UIViewController, source: UIViewController
    ) -> UIViewControllerAnimatedTransitioning? {
        return TransitioningAnimatorIn()
    }

    func animationController(forDismissed dismissed: UIViewController) -> UIViewControllerAnimatedTransitioning? {
        return TransitioningAnimatorOut()
    }
}

extension HalfScreenPictureViewController {
    // MARK: - Update View

    private func subscribeToIsFetching() {
        isFetchingSubscriber = viewModel.$isFetching
            .receive(on: DispatchQueue.main)
            .sink(receiveValue: { [weak self] isFetching in
                if isFetching {
                    LoaderController.sharedInstance.showLoader()
                    self?.imageTitle.text = "Loading..."
                } else {
                    LoaderController.sharedInstance.removeLoader()
                }
            })
    }

    private func subscribeViewData() {
        viewDataSubscriber = viewModel.$viewData
            .receive(on: DispatchQueue.main)
            .sink(receiveValue: { [weak self] viewData in
                guard let title = viewData?.title, let imgData = viewData?.imgData else { return }
                self?.imageTitle.text = title
                self?.imageView.image = UIImage(data: imgData)
            })
    }

    private func subscribeErrorMessage() {
        errorMessageSubscriber = viewModel.$errorMessage
            .receive(on: DispatchQueue.main)
            .sink(receiveValue: { [weak self] message in
                guard let self = self, let message = message else { return }
                self.alert(message: message, retry: self.viewModel.startFetching)
            })
    }
}

extension HalfScreenPictureViewController {
    // MARK: - Rotating screen

    private func rotateToLandscape() {
        let value = UIInterfaceOrientation.landscapeLeft.rawValue
        UIDevice.current.setValue(value, forKey: "orientation")
    }

    private func rotateToPortrait() {
        let value = UIInterfaceOrientation.portrait.rawValue
        UIDevice.current.setValue(value, forKey: "orientation")
    }
}
