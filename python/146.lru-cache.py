#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start


class LinkedNode:
    def __init__(self, key=None, value=None, nextNode=None, prev=None):
        self.key = key
        self.value = value
        self.next = nextNode


class LRUCache:
    # array won't work because put is not O(1)
    def __init__(self, capacity: int):
        self.head = LinkedNode()  # least recent
        self.key2PrevNodeDict = {}
        self.tail = self.head  # most recent
        self.size = capacity

    def get(self, key: int) -> int:
        if not key in self.key2PrevNodeDict:
            return - 1
        result = self.moveNodeToTailAndUpdateIfValue(key, None)
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.key2PrevNodeDict:
            _ = self.moveNodeToTailAndUpdateIfValue(key, value)
        elif len(self.key2PrevNodeDict) == 0:
            # start from fresh
            self.addNewNodeStart(key, value)
        else:
            # all other cases
            self.addNewNode(key, value)

        # self.printLikeThanos(f"put ({key}, {value})")
        # self.printLikeThanosDict(f"put  ({key}, {value})")

    def moveNodeToTailAndUpdateIfValue(self, key, value):
        if self.tail.key == key:
            if value:
                self.tail.value = value
        elif key == self.head.next.key:
            # Least Recent
            oriValue = self.popHead()
            if not value:
                value = oriValue
            self.addNewNode(key, value)
        else:
            # in the middle
            prevNode = self.key2PrevNodeDict[key]
            # if not prevNode:
            #     print(f"({key},{value})")
            if not value:
                value = prevNode.next.value
            # remove this node from key
            del self.key2PrevNodeDict[key]
            # take out currentNode from linked list
            prevNode.next = prevNode.next.next
            if prevNode.next:
                # update prevNode's in dict
                self.key2PrevNodeDict[prevNode.next.key] = prevNode
            # add this new Node
            self.addNewNode(key, value)

        return self.tail.value

    def addNewNode(self, key, value):
        node = LinkedNode(key, value)

        # change tail
        self.key2PrevNodeDict[key] = self.tail
        self.tail.next = node
        self.tail = node

        # change head

        if len(self.key2PrevNodeDict) > self.size:
            self.popHead()

    def popHead(self):
        if len(self.key2PrevNodeDict) == 1:
            currentHead = self.head.next
            rtn = currentHead.value

            self.head = LinkedNode()  # least recent
            self.key2PrevNodeDict = {}
            self.tail = self.head
            return rtn
        currentHead = self.head.next
        rtn = currentHead.value
        del self.key2PrevNodeDict[currentHead.key]

        self.head.next = self.head.next.next
        self.key2PrevNodeDict[self.head.next.key] = None
        return rtn

    def addNewNodeStart(self, key, value):
        node = LinkedNode(key, value)
        self.key2PrevNodeDict[key] = None  # I don't have previous
        self.head.next = node
        self.tail = node

    def printLikeThanos(self, printOut):
        printOut += f"  head(LRU): {self.head.next.key}  tail(MRU): {self.tail.key}  "
        current = self.head.next
        while current:
            printOut += f"({current.key}, {current.value}) ->"
            current = current.next
        print(printOut)

    def printLikeThanosDict(self, printOut):
        for key in self.key2PrevNodeDict.keys():
            item = self.key2PrevNodeDict[key]
            if item is not None:
                printOut += f"[{key}, {item.key}]"
            else:
                printOut += f"[{key}, None]"
            printOut += " -> "
        print(printOut)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


[3],
[1, 1],
[2, 2],
[3, 3],
[4, 4], pop 1 -> 2, 3, 4
[4], 2, 3, 4
[3], 2, 4, 3
[2], 4, 3, 2
[1], -1
[5, 5], pop 4 -> 3, 2, 5
[1], -1
[2], 2
[3], 3
[4],
[5]
