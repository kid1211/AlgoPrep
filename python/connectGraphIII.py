class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """

    def __init__(self, n):
        # initialize your data structure here.
        self.father = {}
        self.connected = n
        for i in range(1, n + 1):
            self.father[i] = i

    def connect(self, a, b):
        # connect their parent
        aRoot, bRoot = self.find(a), self.find(b)

        if aRoot != bRoot:
            self.connected -= 1
            self.father[aRoot] = bRoot

    def find(self, node):
        path = []

        while self.father[node] != node:
            path += [node]
            node = self.father[node]

        for child in path:
            self.father[child] = node

        return node

    """
    @return: An integer
    """

    def query(self):
        return self.connected
