#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start

from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequent_map = collections.Counter(words)
        heap = []

        for word, count in frequent_map.items():
            heappush(heap, (-count, word))

        res = []
        for _ in range(k):
            if heap:
                _, word = heappop(heap)
                res += [word]
        return res

# not sure wtf


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # print(self.hashWord("aaa"), self.hashWord("a"))
        hashToWord = {}
        for word in words:
            hashVal = self.hashWord(word)
            # length = len(word)
            if hashVal not in hashToWord:
                hashToWord[hashVal] = (0, word)
            else:
                occurrence, _ = hashToWord[hashVal]
                hashToWord[hashVal] = (occurrence - 1, word)

        heap = []
        for key in hashToWord:
            heappush(heap, hashToWord[key])
        # print(heap)
        result = []
        for _ in range(k):
            _, word = heappop(heap)
            result += [word]
        # for
        # quick select
        # print(hashToWord)
        return result

    def hashWord(self, word):
        prime, mod = 31, sys.maxsize // 31

        curr = 0
        for n in word:
            curr *= prime
            curr += ord(n) - ord('a') + 1
            curr %= mod

        return curr


# @lc code=end
["a", "aa", "aaa"] \ n1
["plpaboutit", "jnoqzdute", "sfvkdqf", "mjc", "nkpllqzjzp", "foqqenbey", "ssnanizsav", "nkpllqzjzp", "sfvkdqf", "isnjmy", "pnqsz", "hhqpvvt", "fvvdtpnzx", "jkqonvenhx", "cyxwlef", "hhqpvvt", "fvvdtpnzx", "plpaboutit", "sfvkdqf", "mjc", "fvvdtpnzx", "bwumsj", "foqqenbey", "isnjmy", "nkpllqzjzp", "hhqpvvt", "foqqenbey", "fvvdtpnzx", "bwumsj", "hhqpvvt", "fvvdtpnzx", "jkqonvenhx", "jnoqzdute", "foqqenbey", "jnoqzdute", "foqqenbey", "hhqpvvt", "ssnanizsav", "mjc", "foqqenbey", "bwumsj", "ssnanizsav", "fvvdtpnzx", "nkpllqzjzp",
    "jkqonvenhx", "hhqpvvt", "mjc", "isnjmy", "bwumsj", "pnqsz", "hhqpvvt", "nkpllqzjzp", "jnoqzdute", "pnqsz", "nkpllqzjzp", "jnoqzdute", "foqqenbey", "nkpllqzjzp", "hhqpvvt", "fvvdtpnzx", "plpaboutit", "jnoqzdute", "sfvkdqf", "fvvdtpnzx", "jkqonvenhx", "jnoqzdute", "nkpllqzjzp", "jnoqzdute", "fvvdtpnzx", "jkqonvenhx", "hhqpvvt", "isnjmy", "jkqonvenhx", "ssnanizsav", "jnoqzdute", "jkqonvenhx", "fvvdtpnzx", "hhqpvvt", "bwumsj", "nkpllqzjzp", "bwumsj", "jkqonvenhx", "jnoqzdute", "pnqsz", "foqqenbey", "sfvkdqf", "sfvkdqf"]

[(-9, 7, 'hhqpvvt'), (-9, 9, 'fvvdtpnzx'), (-7, 9, 'foqqenbey'), (-3, 5, 'pnqsz'), (-9, 9, 'jnoqzdute'), (-7, 10, 'jkqonvenhx'), (-5, 6, 'bwumsj'),
 (-2, 10, 'plpaboutit'), (-3, 6, 'isnjmy'), (-3, 3, 'mjc'), (-8, 10, 'nkpllqzjzp'), (-5, 7, 'sfvkdqf'), (0, 7, 'cyxwlef'), (-3, 10, 'ssnanizsav')]
