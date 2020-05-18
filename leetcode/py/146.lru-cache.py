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
        self.head = LinkedNode()  # most reason
        self.key2PrevNodeDict = {}
        self.tail = None  # least recent
        self.size = capacity

    def get(self, key: int) -> int:
        if not key in self.key2PrevNodeDict:
            return -1

        prevNode = self.key2PrevNodeDict[key]
        # print(f'key: {key} prevNode: {prevNode.key} isHead: {self.head}')

        if prevNode != self.head:
            # get my node out first
            currentNode = prevNode.next

            # break chain to skip my node
            prevNode.next = prevNode.next.next

            # now deal with head
            prevHead = self.head.next
            self.head.next = currentNode
            currentNode.next = prevHead

            self.key2PrevNodeDict[prevHead.key] = currentNode
            self.key2PrevNodeDict[currentNode.key] = self.head

        return self.head.next.value

    def put(self, key: int, value: int) -> None:
        if key in self.key2PrevNodeDict:
            return

        # itr = self.head
        # while itr.next:
        #     print(itr.value)
        #     itr = itr.next

        # print(f"adding{key} self.key2PrevNodeDict: {self.key2PrevNodeDict}")
        # if self.head.next:
        #     print(f"head: {self.head.next.key}")

        currentNode = LinkedNode(key, value)

        # first time
        if self.head.next is None or self.tail is None:
            print('first time')
            self.tail = currentNode
            self.head.next = currentNode
            self.key2PrevNodeDict[key] = self.head
        else:
            # print(f"before swap head: {self.head.next.key}")
            # put myself in to front
            currentNode.next = self.head.next
            self.head.next = currentNode
            # print(f"after swap head: {self.head.next.key}")

            # update the prev of previous head
            self.key2PrevNodeDict[currentNode.next.key] = currentNode
            self.key2PrevNodeDict[key] = self.head

        if len(self.key2PrevNodeDict) > self.size:
            tailPrev = self.key2PrevNodeDict[self.tail.key]
            # print(
            #     f"key: {key} tailKey: {self.tail.key} Tail's Prev: {tailPrev.value}")
            del self.key2PrevNodeDict[self.tail.key]

            self.tail = tailPrev
            self.tail.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


test get
["LRUCache", "put", "put", "get", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [1], [2], [1]]


cache.put(1, 1)
cache.put(2, 2)
cache.get(1)  # returns 1
cache.put(3, 3)  # evicts key 2
cache.get(2)  # returns - 1 (not found)
cache.put(4, 4)  # evicts key 1
cache.get(1)  # returns - 1 (not found)
cache.get(3)  # returns 3
cache.get(4)  # returns 4

# [null, null, null, 1, null, 2, null, 1, 3, 4]
# [null, null, null, 1, null, -1, null, -1, 3, 4]
