class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for prod in products:
            trie.insert(prod)

        res = []
        prefix = ""
        for c in searchWord:
            prefix += c
            res += [trie.querySuggestions(prefix)]
        return res


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
        self.val = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def querySuggestions(self, prefix):
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            if not node:
                return []

        # get three
        res = []
        self.findWord(node, res)
        return res

    def findWord(self, node, res):
        # this need to be first, this causes the lixxxsafdasfa error
        if len(res) == 3:
            return

        if node.isWord:
            res.append(node.val)

        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in node.children:
                self.findWord(node.children[c], res)

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True
        node.val = word
