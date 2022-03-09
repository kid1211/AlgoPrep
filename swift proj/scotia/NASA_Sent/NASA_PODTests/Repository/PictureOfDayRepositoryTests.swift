//
//  PictureOfDayRepositoryTests.swift
//  NASA_PODTests
//
//  Created by Xujie Zheng on 2020-08-30.
//  Copyright © 2020 Xujie Zheng. All rights reserved.
//

import XCTest
import Combine

// Intergration test
class PictureOfDayRepositoryTests: XCTestCase {

    private var cancellable: AnyCancellable?

    // This might not always pass, depend on if NASA updated frequent enough
    func testGivenTodayByUsingDefault_WhenRepositoryFetch_ThenGetData() {
        let repo = PictureOfDayRepository()
        let exp = expectation(description: "wait for NASA API call to finish")
        var isError: Bool?
        var data: PictureOfTheDayWithPicture?


        cancellable = repo.getPODBaseInfo(date: nil, hd: nil)?
            .sink(
            receiveCompletion: { status in
                switch status {
                case .failure(_):
                    isError = true
                case .finished:
                    isError = false
                }
                exp.fulfill()
            },
            receiveValue: { data = $0 }
        )

        waitForExpectations(timeout: 5, handler: nil)
        XCTAssertFalse(isError ?? false)
        XCTAssertNotNil(data)
    }

    func testGivenInThePast_WhenRepositoryFetch_ThenGetData() {
        let repo = PictureOfDayRepository()
        let exp = expectation(description: "wait for NASA API call to finish")
        var isError: Bool?
        var data: PictureOfTheDayWithPicture?


        cancellable = repo.getPODBaseInfo(date: "2019-08-22", hd: nil)?
            .sink(
            receiveCompletion: { status in
                switch status {
                case .failure(_):
                    isError = true
                case .finished:
                    isError = false
                }
                exp.fulfill()
            },
            receiveValue: { data = $0 }
        )

        waitForExpectations(timeout: 5, handler: nil)
        XCTAssertFalse(isError ?? false)
        XCTAssertNotNil(data)
    }

    func testGivenInTheFuture_WhenRepositoryFetch_ThenGetData() {
        let repo = PictureOfDayRepository()
        let exp = expectation(description: "wait for NASA API call to finish")
        var isError: Bool?
        var data: PictureOfTheDayWithPicture?


        cancellable = repo.getPODBaseInfo(date: "2022-08-22", hd: nil)?
            .sink(
            receiveCompletion: { status in
                switch status {
                case .failure(_):
                    isError = true
                case .finished:
                    isError = false
                }
                exp.fulfill()
            },
            receiveValue: { data = $0 }
        )

        waitForExpectations(timeout: 5, handler: nil)
        XCTAssertTrue(isError ?? false)
        XCTAssertNil(data)
    }

}
