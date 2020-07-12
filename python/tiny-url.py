import random


class TinyUrl:
    def __init__(self):
        self.short2Long = {}
        self.long2Short = {}
    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """

    def longToShort(self, url):
        # write your code here
        if url not in self.long2Short:
            short = self.fiveDigits()

            while short in self.short2Long:
                short = self.fiveDigits()

            self.long2Short[url] = short
            self.short2Long[short] = url

        return "http://tiny.url/" + self.long2Short[url]
    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """

    def shortToLong(self, url):
        # write your code here
        return self.short2Long.get(url.replace("http://tiny.url/", ""))

    def fiveDigits(self):
        canadiates = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n = len(canadiates) - 1

        res = ""
        for _ in range(6):
            res += canadiates[random.randint(0, n)]

        return res
