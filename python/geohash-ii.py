class GeoHash:
    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """

    def decode(self, geohash):
        # write your code here
        # 32 save it in the hashmap if you want
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        maps = {}
        for i in range(32):
            maps[_base32[i]] = f"{i//16%2}{i//8%2}{i//4%2}{i//2%2}{i%2}"
        print(maps)
        # ('110100101100010', '101110001100100')
        lon, lat = "", ""
        isLon = True
        for letter in geohash:
            _5digits = maps[letter]

            for l in _5digits:
                if isLon:
                    lon += l
                    isLon = False
                else:
                    lat += l
                    isLon = True

        return [self.get_location(-90.0, 90.0, lat), self.get_location(-180.0, 180.0, lon)]

    def get_location(self, start, end, string):
        for c in string:
            mid = (start + end) / 2.0
            if c == '1':
                start = mid
            else:
                end = mid
        return (start + end) / 2.0
# "wx4g0s"
