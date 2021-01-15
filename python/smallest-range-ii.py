class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        mi, ma = A[0] + K, A[-1] - K
        ans = A[-1] - A[0]
        
        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            ans = min(ans, max(ma, a+K) - min(mi, b-K))
        return ans
    
# always have +K on the left side and -K on the right side
# then take the difference, some cases are included