//
//  SpinnerViewController.swift
//  NASA_POD
//
//  Source: https://codereview.stackexchange.com/questions/150300/showing-activity-indicator-loading-image-while-processing-in-background
//  Created by Xujie Zheng on 2020-08-29.
//  Copyright © 2020 Xujie Zheng. All rights reserved.
//

import Foundation
import UIKit

class LoaderController: NSObject {
    // MARK: - Properties

    static let sharedInstance = LoaderController()
    private let activityIndicator = UIActivityIndicatorView()

    //MARK: - Methods

    func showLoader() {
        let windows = UIApplication.shared.windows

        setupLoader()
        guard
            windows.count > 0,
            let holdingView =  windows[0].rootViewController?.view
            else { return }

        DispatchQueue.main.async {
            self.activityIndicator.center = holdingView.center
            self.activityIndicator.startAnimating()
            holdingView.addSubview(self.activityIndicator)
            UIApplication.shared.beginIgnoringInteractionEvents()
        }
    }

    func removeLoader(){
        DispatchQueue.main.async {
            self.activityIndicator.stopAnimating()
            self.activityIndicator.removeFromSuperview()
            UIApplication.shared.endIgnoringInteractionEvents()
        }
    }
}

extension LoaderController {
    //MARK: - Helpers

    private func setupLoader() {
        removeLoader()

        activityIndicator.hidesWhenStopped = true
        activityIndicator.style = .gray
    }
}
