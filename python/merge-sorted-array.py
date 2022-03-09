class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1

        for idx in range(len(nums1) - 1, -1, -1):
            # exit case
            if not nums2:
                return
            elif i < 0:
                nums1[idx] = nums2.pop()
                continue

            if nums1[i] < nums2[-1]:
                nums1[idx] = nums2.pop()
            else:
                nums1[idx] = nums1[i]
                i -= 1
                # check which is larger

        # if not nums2 and i still have value, it is all sorted
