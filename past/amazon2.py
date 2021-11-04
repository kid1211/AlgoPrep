def main(arr):
    lastPosition = {}
    n = len(arr)
    for i in range(n):
        lastPosition[arr[i]] = i

    res = []
    left = right = 0
    for i in range(n):
        right = max(right, lastPosition[arr[i]])

        if right == i:
            res.append(right - left + 1)
            left = right + 1

    return res


if __name__ == "__main__":
    res = main(['a', 'b', 'a', 'b', 'c', 'b', 'a', 'c', 'a', 'd', 'e', 'f',
                'e', 'g', 'd', 'e', 'h', 'i', 'j', 'h', 'k', 'l', 'i', 'j'])
    # res = main(['a', 'b', 'a', 'b', 'c'])
    # res = main(['a', 'b', 'c'])
    print(res)
