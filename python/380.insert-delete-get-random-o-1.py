#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = []
        self.idxMap = {}
        # self.getRandom()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.idxMap:
            return False
        self.numbers.append(val)
        self.idxMap[val] = len(self.numbers) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.idxMap or len(self.numbers) == 0:
            return False

        idx = self.idxMap[val]
        del self.idxMap[val]

        lastElement = self.numbers.pop()

        if idx >= len(self.numbers):
            return True

        self.numbers[idx] = lastElement
        self.idxMap[lastElement] = idx

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        temp = random.randint(0, len(self.numbers) - 1)
        return self.numbers[temp]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
