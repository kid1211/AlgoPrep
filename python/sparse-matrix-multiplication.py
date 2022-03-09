# either bruteforce or use this smarter way,
# if using this way, make sure you draw down where is one value is being used
# recommending trying the middle ones


class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def multiply(self, A, B):
        # check edge case

        # row of results is row of A
        # col of results is col of B
        rows = len(A)
        cols = len(B[0])
        results = [[0 for _ in range(cols)] for _ in range(rows)]

        for aRow in range(len(A)):
            for aCol in range(len(A[aRow])):
                if A[aRow][aCol] == 0:
                    continue

                for l in range(len(B[aRow])):
                    results[aRow][l] += A[aRow][aCol] * B[aCol][l]

        return results


#         # [0,0]
#         # # A[Row1]*B[Col1]     A[Row1]*B[Col2]     A[Row1]*B[Col3]
#         # # A[Row2]*B[Col1]     A[Row2]*B[Col1]     A[Row2]*B[Col1]

#         # (0,0)*(0,0) (0,0)(0,1) (0,0)(0,2)
#         (1, 0)


#         (1,0)(1)   (1, 0)  (1,0)

# # [[1,2,3,4,5,6,7],[7,6,5,4,3,2,1]]
# # [[1],[1],[2],[2],[2],[3],[8]]


# # [[1,0,0],[-1,0,3]]
# # [[7,0,0],[0,0,0],[0,0,1]]
# # [
# #     [1,0,0],
# #     [-1,0,3]
# # ]

# # [
# #     [7,0,0],
# #     [0,0,0],
# #     [0,0,1]
# # ]
