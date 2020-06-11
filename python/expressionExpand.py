class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):
        # write your code here
        stack = []

        def appendAns(revString, repeat):
            rtn = []
            n = len(revString)
            for _ in range(repeat):
                for i in range(n):
                    rtn += revString[n - i - 1]
            return rtn

        for l in s:
            if l != ']':
                stack.append(l)
            else:
                revString = ""
                while stack[-1] != '[':
                    revString += stack.pop()

                _ = stack.pop()
                repeat = ""
                while len(stack) > 0 and not stack[-1].isalpha() and stack[-1] != '[':
                    repeat += stack.pop()
                stack += appendAns(revString, int(repeat[::-1]))

        return "".join(stack)
