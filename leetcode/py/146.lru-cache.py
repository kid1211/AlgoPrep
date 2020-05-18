class LinkedNode:
    def __init__(self, key=None, value=None, nextNode=None, prev=None):
        self.key = key
        self.value = value
        self.next = nextNode


class LRUCache:
    # array won't work because put is not O(1)
    def __init__(self, capacity: int):
        self.head = LinkedNode()  # most reason
        self.key2PrevNodeDict = {}
        self.tail = None  # least recent
        self.size = capacity

    def moveToHead(self, currentNode):
        # put myself in to front
        currentNode.next = self.head.next
        self.head.next = currentNode

        # update the prev of previous head
        self.key2PrevNodeDict[currentNode.next.key] = currentNode
        self.key2PrevNodeDict[currentNode.key] = self.head

    def get(self, key: int) -> int:
        if not key in self.key2PrevNodeDict:
            return -1

        prevNode = self.key2PrevNodeDict[key]

        if prevNode != self.head:
            # get my node out first
            currentNode = prevNode.next

            if currentNode == self.tail:
                # print(f"key: {key}, tail: {self.tail.key} 44")
                self.tail = prevNode

            # break chain to skip my node
            prevNode.next = prevNode.next.next

            self.moveToHead(currentNode)

        # 2 not workinkg
        current = self.head.next
        while current.next:
            print(f"{key}run {current.key}")
            current = current.next

        return self.head.next.value

    def put(self, key: int, value: int) -> None:
        if key in self.key2PrevNodeDict:
            currentNode = self.key2PrevNodeDict[key].next
            currentNode.value = value
            self.get(key)
            return

        # add new node
        currentNode = LinkedNode(key, value)

        # first time
        if self.head.next is None or self.tail is None:
            # print('first time')
            self.tail = currentNode
            self.head.next = currentNode
            self.key2PrevNodeDict[key] = self.head
            return

        # not first time
        self.moveToHead(currentNode)

        if len(self.key2PrevNodeDict) > self.size:
            print(f"key: {key}, tail: {self.tail.key} 82")

            tailPrev = self.key2PrevNodeDict[self.tail.key]
            # print(
            #     f"key: {key} tailKey: {self.tail.key} Tail's Prev: {tailPrev.value}")
            del self.key2PrevNodeDict[self.tail.key]

            self.tail = tailPrev
            self.tail.next = None

# [3]
# [1, 1]
# [2, 2]
# [3, 3]
# [4, 4] evict 1 -> 4 3 2
# [4] 432
# [3],342
# [2] 234
# [1], -1
# [5, 5] evict 4 523
# [1] - 1,
# [2]  # should return 2, but -1
# [3]  # should return 3
# [4] - 1 didn't evict 4
# [5]
