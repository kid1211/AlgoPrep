class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        res = []
        for item in nestedList:
            if isinstance(item, list):
                res += self.flatten(item)
            else:
                res.append(item)

        return res
