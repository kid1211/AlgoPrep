'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndexs):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndexs, content):
        # Write a chunk to GFS
'''
from random import randint


class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """

    def __init__(self, chunkSize):
        BaseGFSClient.__init__(self)
        self.chunkSize = chunkSize
        self.uniqueIndex = set()  # xx
        self.chunkIndexs = collections.defaultdict(list)

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """

    def read(self, filename):
        # write your code here
        if filename not in self.chunkIndexs:
            return
        res = ""
        for idx in self.chunkIndexs[filename]:
            subRes = BaseGFSClient.readChunk(self, filename, idx)
            if subRes:
                res += subRes

        return res

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """

    def write(self, filename, content):
        if filename in self.chunkIndexs:
            for key in self.chunkIndexs[filename]:
                self.uniqueIndex.discard(key)
            self.chunkIndexs[filename] = []

        while content:
            saving = content[:self.chunkSize]
            content = content[self.chunkSize:]
            idx = self.getIdx()
            self.chunkIndexs[filename].append(idx)
            BaseGFSClient.writeChunk(self, filename, idx, saving)

    def getIdx(self):
        idx = randint(0, 900)
        while idx in self.uniqueIndex:
            idx = randint(0, 900)
        self.uniqueIndex.add(idx)
        return idx
