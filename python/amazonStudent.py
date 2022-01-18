def maxValue(n, rounds):

    temp = []
    for start, end, amount in rounds:
        temp += [(start, amount)]
        temp += [(end + 1, -amount)]

    maxi = curr = 0
    for _, val in sorted(temp):
        curr += val
        maxi = max(maxi, curr)
    return maxi


if __name__ == "__main__":
    tcs = [
        ([[2, 3, 603], [1, 1, 286], [4, 4, 882]], 882),
        ([[1, 2, 10], [2, 4, 5], [3, 5, 12]], 17),
        ([[1, 2, 100], [2, 5, 100], [3, 4, 100]], 200),
        ([[1, 1, 200], [1, 1, 200], [1, 1, 200]], 600),
    ]
    for rounds, val in tcs:
        print(maxValue(2, rounds) == val)
# 2 3 603
# 1 1 286
# 4 4 882

# #
# 1 2 10
# 2 4 5
# 3 5 12

