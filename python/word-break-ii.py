class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        # write your code here

        # because we need to have something to return to store in memoe
        # updated in a way so we can get prefix's correspoinding substring

        # because of that results is no longer needed
        # same as current
        return self.dfs(s, dict, {})

    def dfs(self, s, dict, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        res = []
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if not prefix in dict:
                continue

            # with this prefix what are you getting back
            permutations = self.dfs(s[i:], dict, memo)

            for permu in permutations:
                res.append(prefix + " " + permu)

        if s in dict:
            res.append(s)

        # print(s, res)
        memo[s] = res
        return res


# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
