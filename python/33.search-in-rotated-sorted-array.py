#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        if end < 0:
            return -1
        if end == 0:
            return end if nums[end] == target else -1

        return self.searchWithinRange(nums, target, start, end)

    def searchWithinRange(self, nums, target, start, end):
        print(nums[start: end + 1])
        if start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[end]:
                # pivot on the right [3 ,4, 7, 1, 2]
                if (nums[start] <= target and target <= nums[mid]):
                    return self.searchWithinRange(nums, target, start, mid)
                else:
                    return self.searchWithinRange(nums, target, mid, end)
            else:
                # pivot on the left [12, 2, 4, 7, 9, 10]
                if (nums[mid] <= target and target <= nums[end]):
                    return self.searchWithinRange(nums, target, mid, end)
                else:
                    return self.searchWithinRange(nums, target, start, mid)

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1


# @lc code=end
# [1, 2, 3, 4, 5, 6, 7, 8]
# mid = 4

# target 2
# mid > target
# drop right
# [1, 2, 3, 4, 5, 6, 7, 8] find 2, mid 4,
# -> [1, 2, 3, 4]
# end > target > start

# edge 1
# [7, 8, 9, 10, 11, 2, 4, 5] find 2 , mid 10
# target < end, start < end

# edge 2
# [4, 5, 6, 7, 0, 1, 2] find 1, mid 7
# mid > target drop left
