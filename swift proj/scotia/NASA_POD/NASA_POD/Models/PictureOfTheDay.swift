//
//  PictureOfTheDayDecode.swift
//  NASA_POD
//
//  Created by Xujie Zheng on 2020-08-28.
//  Copyright © 2020 Xujie Zheng. All rights reserved.
//

import Foundation

class NASAPlanetAPIDecode {
    // MARK: - Picture of the Day

    struct PictureOfTheDay: Codable {
        let code: Int?
        let msg: String?
        let service_version: String?

        let copyright: String?
        let date: String?
        let explanation: String?
        let hdurl: String?
        let media_type: String? // Maybe Check this
        let title: String?
        let url: String?
    }
}

// MARK: - Business/App Logic Object

struct PictureOfTheDayWithPicture {
    let date: String?
    let title: String?
    let imgData: Data?
}
