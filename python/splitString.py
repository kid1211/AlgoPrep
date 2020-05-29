class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        results = []
        self.dfs([], s, results)
        return results

    def dfs(self, current, s, results):
        # print(current, s, results)
        if s == "":
            results.append(current[:])
            return

        for i in range(2):
            if i + 1 > len(s):
                return

            current.append(s[:i + 1])
            self.dfs(current, s[i+1:], results)
            current.pop()

# template 2, template 1 is combination such as ksum
# class Solution:
#     """
#     @param: : a string to be split
#     @return: all possible split string array
#     """

#     def splitString(self, s):
#         if s == "":
#             return [[]]
#         return self.dfs2(s)

#     def dfs2(self, s):
#         if s == "":
#             return []

#         rtn = []
#         for i in range(1, len(s) + 1):
#             prefix = s[:i]
#             if len(prefix) > 2:
#                 continue

#             # print(prefix, s[i:])
#             possible = self.dfs2(s[i:])

#             for par in possible:
#                 curr = [prefix]
#                 curr += par
#                 rtn.append(curr)

#         if len(s) <= 2:
#             # print(s)
#             rtn.append([s])

#         return rtn
