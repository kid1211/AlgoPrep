class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []

        def popAndAppend(stack):
            repeat = ""
            while stack[-1] != '[':
                repeat += stack.pop()

            _ = stack.pop()  # pop [

            nums = ""
            while stack and stack[-1].isnumeric():
                nums += stack.pop()

            for _ in range(int(nums[::-1])):
                stack += repeat[::-1]

        for char in s:
            if char != "]":
                stack += char
            else:
                popAndAppend(stack)

        return "".join(stack)


# "3[2[ad]3[pf]]xyz"