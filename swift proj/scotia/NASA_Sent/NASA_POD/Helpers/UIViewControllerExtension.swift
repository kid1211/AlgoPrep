//
//  UIViewController.swift
//  NASA_POD
//
//  Created by Xujie Zheng on 2020-08-29.
//  Copyright © 2020 Xujie Zheng. All rights reserved.
//

import Foundation
import UIKit

extension UIViewController {
    func alert(message: String, retry: @escaping (() -> Void)) {
        let alertController = UIAlertController(title: title, message: message, preferredStyle: .alert)
        let OKAction = UIAlertAction(title: "OK", style: .default, handler: { _ in retry() })
        alertController.addAction(OKAction)
        DispatchQueue.main.async { [weak self] in
            self?.present(alertController, animated: true, completion: nil)
        }
    }
}
