3
1
2

31
312

12


def getTotalImbalance(weight):
    return getExtreme(weight, True) - getExtreme(weight, False)


def getExtreme(weight, isMax):
    def compare(val1, val2):
        return val1 <= val2 if isMax else val1 >= val2

    sums = curr = 0
    stack = []
    length = len(weight)

    for i in range(length):
        val = weight[i]
        print(len(stack))
        while stack and compare(stack[-1][1], val):
            right, ori_sum = stack.pop()
            left = 0 if not stack else stack[-1][0] + 1
            curr -= (right - left + 1) * ori_sum

        left = 0 if not stack else stack[-1][0] + 1
        curr += (i - left + 1) * val
        sums += curr
        stack.append((i, val))
    return sums


# def getTotalImbalance(weight):
#     results = []
#     dfs(sorted(weight), 0, [], results)

#     print(results)
#     sums = 0
#     for res in results:
#         sums += max(res) - min(res)

#     return sums


# def dfs(weight, index, current, results):
#     if index >= len(weight):
#         results += [current]
#         return

#     for i in range(index, len(weight)):
#         dfs(weight, i + 1, current + [weight[i]], results)


print(getTotalImbalance([3, 2, 1]))

