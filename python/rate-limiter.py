class Solution:
    def __init__(self):
        self.maps = {}
    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """

    def isRatelimited(self, timestamp, event, rate, increment):
        # write your code here
        # start = rate.find("/")
        # total_time = int(rate[:start])
        # type = rate[start+1:]
        count, timeType = rate.split('/')

        time = 1
        if timeType == 'm':
            time *= 60
        elif timeType == 'h':
            time *= 60 * 60
        elif timeType == 'd':
            time *= 60 * 60 * 24

        validBegin = timestamp - time + 1

        # create entry
        if event not in self.maps:
            self.maps[event] = []

        # binary search check fromt he beinign times to now, how many events?
        isRateLimited = self.countEvents(
            self.maps[event], validBegin) >= int(count)
        if increment and not isRateLimited:
            self.maps[event].append(timestamp)

        return isRateLimited

    def countEvents(self, event, ts):
        left, right = 0, len(event)

        if not event or event[-1] < ts:
            return 0

        while left <= right:
            mid = (left + right) // 2

            if event[mid] >= ts:
                # valid
                right = mid - 1
            else:
                left = mid + 1

        # return left if nums[left] == target else -1
        if event[left] >= ts:
            return len(event) - left
        else:
            return 0
