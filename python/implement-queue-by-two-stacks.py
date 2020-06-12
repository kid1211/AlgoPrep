class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.backward, self.forward = [], []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        self.backward.append(element)

    """
    @return: An integer
    """

    def pop(self):
        self.compressStack()

        if self.forward:
            return self.forward.pop()
        return -1

    """
    @return: An integer
    """

    def top(self):
        self.compressStack()
        return self.forward[-1] if self.forward else -1

    def compressStack(self):
        if not self.forward:
            while self.backward:
                self.forward.append(self.backward.pop())
