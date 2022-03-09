//
//  FullScreenPictureViewController.swift
//  NASA_POD
//
//  Created by Xujie Zheng on 2020-08-29.
//  Copyright © 2020 Xujie Zheng. All rights reserved.
//

import Foundation
import UIKit
import Combine

class FullScreenPictureViewController: UIViewController {
    // MARK: - Properties

    @IBOutlet weak var fullScreenImageView: UIImageView!
    @Published var viewData: PictureOfTheDayWithPicture?
    private var viewDataSubscriber: AnyCancellable?
    var beforeDismiss: (() -> Void)? // Probably there is a better way

    // MARK: - Life Cycle

    override func viewDidLoad() {
        setupView()
        subscribeViewData()
        self.fullScreenImageView.transform = CGAffineTransform(rotationAngle: CGFloat(Double.pi/2))
    }

    deinit {
        viewDataSubscriber?.cancel()
    }
    
    // MARK: - Helpers

    private func setupView() {
        let tapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(imageTapped(tapGestureRecognizer:)))
        fullScreenImageView.isUserInteractionEnabled = true
        fullScreenImageView.addGestureRecognizer(tapGestureRecognizer)
    }

    @objc func imageTapped(tapGestureRecognizer: UITapGestureRecognizer) {
        beforeDismiss?()
        dismiss(animated: true)
    }
}

extension FullScreenPictureViewController {
    private func subscribeViewData() {
        viewDataSubscriber = $viewData
            .receive(on: DispatchQueue.main)
            .sink(receiveValue: { [weak self] viewData in
                guard let self = self, let imgData = viewData?.imgData else { return }
                self.fullScreenImageView.image = UIImage(data: imgData)
            })
    }
}
