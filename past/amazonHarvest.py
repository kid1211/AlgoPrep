def maxHarvest(arr, k):
    n = len(arr)
    maxProfit = float("-inf")

    # Evaluate all n/2 harvesting options (6 slices->3 options, 4 slices->2 options, and so on)
    # print(n // 2)
    for i in range(n // 2):
        sm = 0
        for j in range(k):
            currIndex = i + j
            oppositeIndex = (
                currIndex + (n // 2) % n
            )  # adding n//2 gets us the opposite slice's index. %2 for wrapping around array
            # print(oppositeIndex)
            sm += arr[currIndex] + arr[oppositeIndex]
        maxProfit = max(maxProfit, sm)

    return maxProfit


# better ^
import sys


def maxHarvest(arr, k):
    global res
    res = -sys.maxsize + 1

    n = len(arr) // 2

    can = []
    for i in range(n):
        can += [arr[i] + arr[i + n]]

    dfs(can, k, 0, [])
    return res


def dfs(arr, k, index, current):
    if len(current) > k:
        return

    if len(current) == k:
        global res
        res = max(res, sum(current))
        return

    for i in range(index, len(arr)):
        dfs(arr, k, i + 1, current + [arr[i]])


print("0-000000000000000000000000000000")
# print(maxHarvest([3, -5], 1))  # -2
print(maxHarvest([1, 5, 1, 3, 7, -3, 10, 22, 33, 43], 2))  # 16

# print(maxHarvest([-6, 3, 6, -3], 1))  # 0

print("0-000000000000000000000000000000")

# 7
# 10 = > 5 * 2

# # 3 * 2 = 6
#  15 = >


# yo
# yo
# yo
# yo
# yo
# yo
# yo
# yo
# yo
# yo
# yo
# yo
# yo
# yo
# yo
# yo
