def main(arr, K):
    def isValid(arr):
        unique = {}

        for item in arr:
            unique[item] = unique.get(item, 0) + 1
        return len(unique) == K - 1

    res = set()
    n = len(arr)
    unique = {}
    if n < K:
        return []

    for i in range(K, n + 1):
        if isValid(arr[i - K:i]):
            res.add(arr[i - K:i])

    return list(res)


if __name__ == "__main__":
    # res = main("democracy", 5)
    res = main("wawaglknagagwunagkwkwagl", 4)
    print(res)
