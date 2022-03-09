//
//  APODRepository.swift
//  NASA_POD
//
//  Source: https://theswiftdev.com/urlsession-and-the-combine-framework/
//  Source2: https://www.donnywals.com/using-map-flatmap-and-compactmap-in-combine/
//
//  Created by Xujie Zheng on 2020-08-28.
//  Copyright © 2020 Xujie Zheng. All rights reserved.
//

import Foundation
import Combine

protocol NASARepository {
    // https://api.nasa.gov/?search=APOD
    // date in YYYY-MM-DD Format, hd high definetion of Picture
    func getPODBaseInfo(date: String?, hd: Bool?) -> AnyPublisher<PictureOfTheDayWithPicture, Error>?
}

class PictureOfDayRepository: NASARepository {
    // MARK: - Properties

    private let BASE_URL = "https://api.nasa.gov/planetary/apod"
    private let API_KEY = "NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo"
    lazy var urlSession = {
        URLSession.shared
    }()

    // MARK: - Methods

    func getPODBaseInfo(date: String?, hd: Bool?) -> AnyPublisher<PictureOfTheDayWithPicture, Error>?  {
        // Use Charles Proxy to mock Data
        guard let url = generateURL(date: date, hd: hd) else { return nil }
        return urlSession
        .dataTaskPublisher(for: url)
        .tryMap() { element -> Data in
            guard let httpResponse = element.response as? HTTPURLResponse,
                httpResponse.statusCode == 200 || httpResponse.statusCode == 202 else {
                    throw URLError(.badServerResponse)
                }
            return element.data
            }
        .decode(type: NASAPlanetAPIDecode.PictureOfTheDay.self, decoder: JSONDecoder())
        .tryMap() { element -> NASAPlanetAPIDecode.PictureOfTheDay in
            guard element.url != nil && element.url != "" else { throw URLError(.badServerResponse) }
            return element
        }
        .flatMap { self.fetchPicture(with: $0) }
        .eraseToAnyPublisher()
    }
}

extension PictureOfDayRepository {
    // MARK: - Helper

    private func fetchPicture(with basicInfo: NASAPlanetAPIDecode.PictureOfTheDay) -> AnyPublisher<PictureOfTheDayWithPicture, Error> {
        let url = URL(string: basicInfo.url!)! // move this to the model
        return urlSession.dataTaskPublisher(for: url)
            .mapError { $0 as Error }
            .map {
                PictureOfTheDayWithPicture(date: basicInfo.date, title: basicInfo.title, imgData: $0.data)
            }
            .eraseToAnyPublisher()
    }

    private func generateURL(date: String?, hd: Bool?) -> URL? {
        var url = "\(BASE_URL)?api_key=\(API_KEY)"

        if let date = date {
            url += "&date=\(date)"
        }

        if let hd = hd {
            url += "&hd=\(hd)"
        }

        return URL(string: url)
    }
}

