class Memcache:
    def __init__(self):
        # do intialization if necessary
        self.mem = {}

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """

    def get(self, curtTime, key):
        # write your code here

        if key in self.mem:
            expired, val = self.mem[key]
            if expired == 0 or curtTime <= expired:
                return val
            else:
                self.delete(curtTime, key)
        return 2147483647

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """

    def set(self, curtTime, key, value, ttl):
        # write your code here
        expired = 0 if ttl == 0 else curtTime + ttl - 1
        self.mem[key] = (expired, value)

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """

    def delete(self, curtTime, key):
        # write your code here
        # maybe need to check
        if key in self.mem:
            del self.mem[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """

    def incr(self, curtTime, key, delta):
        # write your code here
        if key not in self.mem:
            return 2147483647

        ttl, val = self.mem[key]
        val += delta
        self.mem[key] = (ttl, val)
        return val

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """

    def decr(self, curtTime, key, delta):
        # write your code here
        return self.incr(curtTime, key, -delta)
