//
//  HalfScreenPictureViewModel.swift
//  NASA_POD
//
//  Created by Xujie Zheng on 2020-08-29.
//  Copyright © 2020 Xujie Zheng. All rights reserved.
//

import Foundation
import Combine

class HalfScreenPictureViewModel {
    // MARK: - Properties

    private var pictureOfDayRepository: NASARepository
    private var cancellable: AnyCancellable?
    @Published private(set) var isFetching: Bool = false
    @Published private(set) var viewData: PictureOfTheDayWithPicture?
    @Published private(set) var errorMessage: String?

    // MARK: - Method

    init(repository: NASARepository = PictureOfDayRepository()) {
        pictureOfDayRepository = repository
    }

    deinit {
        cancellable?.cancel()
    }

    public func startFetching() {
        isFetching = true
        cancellable = pictureOfDayRepository.getPODBaseInfo(date: nil, hd: nil)?.sink(
            receiveCompletion: { [weak self] status in
                switch status {
                case .failure(_):
                    self?.handleGenericError()
                case .finished:
                    break
                }

                self?.isFetching = false
            },
            receiveValue: { [weak self] data in
                if data.title != nil, data.imgData != nil {
                    self?.viewData = data
                    self?.errorMessage = nil
                } else {
                    self?.handleGenericError()
                }
            })
    }

    private func handleGenericError() {
        viewData = nil
        errorMessage = "Something went wrong with the Network service, try reopen the app."
    }
}
