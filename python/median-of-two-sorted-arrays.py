class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        if len(A) > len(B):
            nums1, nums2 = B, A
        else:
            nums1, nums2 = A, B

        # 如果是偶数 左边最大值和右边最小值的平均数
        # 如果是基数 左边的最大值是中位数
        n, m = len(nums1), len(nums2)
        isEven = (n + m) % 2 == 0
        minSize = -((n + m) // -2)  # get how many should be on the left

        # binary search on n
        # normally left + 1 < right, so, 0, n - 1
        # now left <= right, 0, n
        left, right = 0, n  # !!diff
        # this means left and right will go over itself
        while left <= right:  # !!diff
            print(left, right)
            # if we want L1 mid -1, r1, mid
            # then nMid represent how many items already on the left
            nMid = (left + right) // 2
            mMid = minSize - nMid

            L1 = nums1[nMid - 1] if nMid != 0 else -sys.maxsize + 1
            L2 = nums2[mMid - 1] if mMid != 0 else -sys.maxsize + 1
            R1 = nums1[nMid] if nMid != n else sys.maxsize
            R2 = nums2[mMid] if mMid != m else sys.maxsize

            if L1 > R2:
                # avoid 1<=2 situation
                # because l1 is nMid - 1
                right = nMid - 1  # !!diff
            elif L2 > R1:
                # because L2 is mMid - 1
                left = nMid + 1  # !!diff
            else:
                # found it
                if (n + m) % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                else:
                    return max(L1, L2)

        return -1
