class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        unique = {}
        res = []
        n = len(A)
        j = 0

        def exceedAdd(j, unique, res):
            while j < n and (A[j] in unique or len(unique) <= K):
                unique[A[j]] = unique.get(A[j], 0) + 1
                j += 1

                if len(unique) == K:
                    res.append(A[i:j])

        for i in range(n):
            while j < n and len(unique) < K:
                unique[A[j]] = unique.get(A[j], 0) + 1
                j += 1

            if len(unique) == K:
                res.append(A[i:j])

            exceedAdd(j, dict(unique), res)

            unique[A[i]] -= 1
            if unique[A[i]] == 0:
                del unique[A[i]]

        return len(res)
