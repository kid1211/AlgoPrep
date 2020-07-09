class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        # write your code here
        hashmap = collections.defaultdict(list)

        for word in strs:
            hashmap["".join(sorted(word))].append(word)

        res = []
        for _, items in hashmap.items():
            if len(items) > 1:
                res += items

        return res
