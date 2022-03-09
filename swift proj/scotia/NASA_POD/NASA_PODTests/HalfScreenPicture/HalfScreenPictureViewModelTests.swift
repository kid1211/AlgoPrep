//
//  HalfScreenPictureViewModelTests.swift
//  NASA_PODTests
//
//  Created by Xujie Zheng on 2020-08-29.
//  Copyright © 2020 Xujie Zheng. All rights reserved.
//

import Foundation
import Combine
import XCTest

@testable import NASA_POD

class HalfScreenPictureViewModelTests: XCTestCase {

    func test_GivenSubscriptionOnViewData_WhenRepositoryPublishData_ThenViewDataIsNotNil() {
        // Given
        let mockRepository = MockRepository()
        let viewModel = HalfScreenPictureViewModel(repository: mockRepository)
        let mockViewData = PictureOfTheDayWithPicture(date: "2020-08-12", title: "Picture", imgData: Data())

        // When
        viewModel.startFetching()
        mockRepository.publisher.send(mockViewData)

        // Then
        var imageData: Data?
        var date: String?
        var title: String?

        _ = viewModel.$viewData
            .compactMap { $0 }
            .sink { viewData in
                imageData = viewData.imgData
                date = viewData.date
                title = viewData.title
            }

        XCTAssertNotNil(imageData)
        XCTAssertEqual(date, mockViewData.date)
        XCTAssertEqual(title, mockViewData.title)
    }

    func test_GivenSubscriptionFailure_WhenRepositoryPublishData_ThenErrorMessageNotNil() {
        // Given
        let mockRepository = MockRepository()
        let viewModel = HalfScreenPictureViewModel(repository: mockRepository)
        let mockError = URLError(.badServerResponse)

        // When
        viewModel.startFetching()
        mockRepository.publisher.send(completion: .failure( mockError ))

        // Then
        var errorMessage: String?

        _ = viewModel.$errorMessage
            .compactMap { $0 }
            .sink { error in
                errorMessage = error
            }

        XCTAssertEqual(errorMessage, "Something went wrong with the Network service, try reopen the app.")
    }

    func test_GivenSubscriptionIfNotFetching_WhenRepositoryPublishData_ThenIsFetchingUpdated() {
        // Given
        let mockRepository = MockRepository()
        let viewModel = HalfScreenPictureViewModel(repository: mockRepository)
        let mockError = URLError(.badServerResponse)
        var isFetching: Bool?
        let getIsFetching = {
            _ = viewModel.$isFetching
                .compactMap { $0 }
                .sink { isFetching = $0 }
        }

        // When
        getIsFetching()
        XCTAssertFalse(isFetching!) // Before Fetching

        viewModel.startFetching()

        getIsFetching()
        XCTAssertTrue(isFetching!) // During Fetching

        mockRepository.publisher.send(completion: .failure( mockError ))

        // Then

        getIsFetching()
        XCTAssertFalse(isFetching!) // After Fetching
    }
}

extension HalfScreenPictureViewModelTests {
    class MockRepository: NASARepository {
        let publisher = PassthroughSubject<PictureOfTheDayWithPicture, Error>()
        func getPODBaseInfo(date: String?, hd: Bool?) -> AnyPublisher<PictureOfTheDayWithPicture, Error>? {
            return publisher.eraseToAnyPublisher()
        }
    }
}

