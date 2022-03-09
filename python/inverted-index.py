'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''


class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        # Write your code here
        maps = collections.defaultdict(set)

        for doc in docs:
            for word in doc.content.split():
                maps[word].add(doc.id)

        ans = {}
        for key in maps:
            ans[key] = sorted(maps[key])
        return ans
