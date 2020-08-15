def main(arr, K):
    def isValid(arr):
        localUnique = {}

        for item in arr:
            localUnique[item] = localUnique.get(item, 0) + 1
        return len(localUnique) == K - 1

    res = set()
    n = len(arr)
    uniques = {}
    if n < K:
        return []

    unique = {}
    for i in range(K):
        unique[arr[i]] = unique.get(arr[i], 0) + 1

    for i in range(K, n):

        unique[arr[i]] = unique.get(arr[i], 0) + 1
        unique[arr[i - K]] -= 1
        if unique[arr[i - K]] == 0:
            del unique[arr[i - K]]

        if len(unique) == K - 1:
            res.add(arr[i - K + 1:i + 1])

    return list(res)


if __name__ == "__main__":
    res = main("democracy", 5)
    # res = main("wawaglknagagwunagkwkwagl", 4)
    print(res)
