class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """

    def submatrixSum(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return None
        rows, cols = len(matrix), len(matrix[0])

        for top in range(rows):
            # init
            arr = [0 for _ in range(cols)]

            for row in range(top, rows):
                # start from -1, which is start
                prefixHash = {0: -1}
                prefixSum = 0  # rolling sum for this row only
                # read about the array oen first https://www.lintcode.com/problem/subarray-sum-equals-k/description
                for col in range(cols):
                    arr[col] += matrix[row][col]
                    prefixSum += arr[col]

                    if prefixSum in prefixHash:
                        # [-5, 1, 1, 5, -7] -> [-5, -4, -3, 2, -5]
                        # when we computed the last -5, we know -5 is already in the hashmap, and saved at col 0
                        # we want sums[4] - sums[0] = 0, our array should be [1 -> 4] [a, b, c] ->  b, c => sum[c] - sum[a]
                        # sums[0] represent everything before 1, so when we do the line above make sense
                        return [[top, prefixHash[prefixSum] + 1], [row, col]]
                    prefixHash[prefixSum] = col  # save the col index
                print(prefixHash)
        return None

# [[3,7,-8],[1,5,7],[4,-8,9]]

# [[0, 1],[1, 0]] what is the {0, -1}

# [[1, 5, 7],[3, 7, -8],[4, -8 ,9]]
