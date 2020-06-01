class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        dis = {}
        n = len(s)
        j = 0
        longest = 0
        maxDistinc = len(set([l for l in s]))

        if s is "":
            return 0
        if maxDistinc <= k:
            return len(s)

        for i in range(n):
            while j < n and (len(dis) < k or s[j] in dis):
                letter = s[j]
                if letter in dis:
                    dis[letter] += 1
                else:
                    dis[letter] = 1
                j += 1

            if len(dis) >= k:
                print(s[i: j], len(dis))
                longest = max(longest, j - i)

            takeOut = s[i]

            if takeOut in dis:
                occurence = dis[takeOut]
                if occurence - 1 == 0:
                    del dis[takeOut]
                else:
                    dis[takeOut] = occurence - 1

        if longest == 0:
            return min(k, maxDistinc)
        else:
            return longest

# "eceba"
# 3

# "eqgkcwGFvjjmxutystqdfhuMblWbylgjxsxgnoh"
# 16
# "nfhiexxjrtvpfhkrxcutexxcodfioburrtjefrgwrnqtyzelvtpvwdvvpsbudwtiryqzzy"
# 25
