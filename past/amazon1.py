def main(arr, K):
    # def isValid(arr):
    #     localUnique = {}

    #     for item in arr:
    #         localUnique[item] = localUnique.get(item, 0) + 1
    #     return len(localUnique) == K - 1

    res = set()
    n = len(arr)
    uniques = {}
    if n < K:
        return []

    unique = {}
    # for i in range(K):
    #     unique[arr[i]] = unique.get(arr[i], 0) + 1

    j = 0
    for i in range(n):
        while j < n and j < i + K and (arr[j] in unique or len(unique) < K - 1):
            unique[arr[j]] = unique.get(arr[j], 0) + 1
            j += 1

        if len(unique) == K - 1 and j == i + K:
            res.add(arr[i:j])

        unique[arr[i]] -= 1
        if unique[arr[i]] == 0:
            del unique[arr[i]]

    return list(res)


if __name__ == "__main__":
    res = main("democracy", 5)
    # res = main("wawaglknagagwunagkwkwagl", 4)
    print(res)
