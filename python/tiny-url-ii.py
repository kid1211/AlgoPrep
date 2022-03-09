import random


class TinyUrl2:
    def __init__(self):
        self.short2Long = {}
        self.long2Short = {}
    """
    @param: long_url: a long url
    @param: key: a short key
    @return: a short url starts with http://tiny.url/
    """

    def createCustom(self, long_url, key):
        # write your code here
        if key in self.short2Long and long_url != self.short2Long[key]:
            return 'error'
        if long_url in self.long2Short and key != self.long2Short[long_url]:
            return 'error'
        self.short2Long[key] = long_url
        self.long2Short[long_url] = key
        return "http://tiny.url/" + key

    """
    @param: long_url: a long url
    @return: a short url starts with http://tiny.url/
    """

    def longToShort(self, long_url):
        # write your code here
        if long_url not in self.long2Short:
            short = self.fiveDigits()

            while short in self.short2Long:
                short = self.fiveDigits()

            self.long2Short[long_url] = short
            self.short2Long[short] = long_url

        return "http://tiny.url/" + self.long2Short[long_url]
    """
    @param: short_url: a short url starts with http://tiny.url/
    @return: a long url
    """

    def shortToLong(self, short_url):
        # write your code here
        return self.short2Long.get(short_url.replace("http://tiny.url/", ""))

    def fiveDigits(self):
        canadiates = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n = len(canadiates) - 1

        res = ""
        for _ in range(6):
            res += canadiates[random.randint(0, n)]

        return res
