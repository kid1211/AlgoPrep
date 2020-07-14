class GeoHash:
    """
    @param: latitude: one of a location coordinate pair 
    @param: longitude: one of a location coordinate pair 
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """

    def encode(self, latitude, longitude, precision):
        # write your code here
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"  # 32
        lat, lon = self.gethash(
            latitude, -90, 90), self.gethash(longitude, -180, 180)

        # 4 digits is one letter
        res = ''

        latIdx, lonIdx = 0, 0
        # res lenght is 12
        for _ in range(precision):
            _binary = ""
            while len(_binary) <= 4:
                if lonIdx <= latIdx:
                    _binary += lon[lonIdx]
                    lonIdx += 1
                else:
                    _binary += lat[latIdx]
                    latIdx += 1

            res += _base32[int(_binary, 2)]

        return res

    def gethash(self, value, start, end):
        res = ''

        for _ in range(30):
            mid = (start + end) / 2

            if value > mid:
                res += '1'
                start = mid
            else:
                res += '0'
                end = mid
        return res
