# https://leetcode.com/discuss/interview-question/762546/
import sys


def main(codeList, shoppingCart):

    pass


def dfs(code, idx1, shoppingCart, idx2):
    if len(code) == idx1:
        return True

    if code[idx1] != shoppingCart[idx2]:
        return self.dfs(code, 0, shoppingCart, idx2 + 1)
    pass


def test(codeList1, shoppingCart1, res):
    return main(codeList1, shoppingCart1) == res


if __name__ == "__main__":

    codeList1 = [["apple", "apple"], ["banana", "anything", "banana"]]
    shoppingCart1 = ["orange", "apple", "apple", "banana", "orange", "banana"]
    codeList2 = [["apple", "apple"], ["banana", "anything", "banana"]]
    shoppingCart2 = ["banana", "orange", "banana", "apple", "apple"]
    codeList3 = [["apple", "apple"], ["banana", "anything", "banana"]]
    shoppingCart3 = ["apple", "banana", "apple", "banana", "orange", "banana"]
    codeList4 = [["apple", "apple"], ["apple", "apple", "banana"]]
    shoppingCart4 = ["apple", "apple", "apple", "banana"]
    codeList5 = [["apple", "apple"], ["banana", "anything", "banana"]]
    shoppingCart5 = ["orange", "apple", "apple", "banana", "orange", "banana"]
    codeList6 = [["apple", "apple"], ["banana", "anything", "banana"]]
    shoppingCart6 = ["apple", "apple", "orange",
                     "orange", "banana", "apple", "banana", "banana"]
    codeList7 = [["anything", "apple"], ["banana", "anything", "banana"]]
    shoppingCart7 = ["orange", "grapes", "apple", "orange",
                     "orange", "banana", "apple", "banana", "banana"]
    codeList8 = [["apple", "orange"], ["orange", "banana", "orange"]]
    shoppingCart8 = ["apple", "orange", "banana",
                     "orange", "orange", "banana", "orange", "grape"]
    codeList9 = [["anything", "anything", "anything",
                  "apple"], ["banana", "anything", "banana"]]
    shoppingCart9 = ["orange", "apple", "banana", "orange",
                     "apple", "orange", "orange", "banana", "apple", "banana"]

    test(codeList1, shoppingCart1, 1)
    test(codeList2, shoppingCart2, 0)
    test(codeList3, shoppingCart3, 0)
    test(codeList4, shoppingCart4, 0)
    test(codeList5, shoppingCart5, 1)
    test(codeList6, shoppingCart6, 1)
    test(codeList7, shoppingCart7, 1)
    test(codeList8, shoppingCart8, 1)
    test(codeList9, shoppingCart9, 1)
