class WebLogger:

    def __init__(self):
        # do intialization if necessary
        self.arr = []
        # need to travese entire thing anyway, no reason to use dict

    """
    @param: timestamp: An integer
    @return: nothing
    """

    def hit(self, timestamp):
        self.arr.append(timestamp)

    """
    @param: timestamp: An integer
    @return: An integer
    """

    def get_hit_count_in_last_5_minutes(self, timestamp):
        # write your code here
        if not self.arr:
            return 0

        for i in range(len(self.arr) - 1, -1, -1):
            if self.arr[i] + 300 <= timestamp:
                self.arr = self.arr[i + 1:]
                break

        return len(self.arr)
