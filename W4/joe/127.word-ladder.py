#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        count = 0
        visited = set()
        queue = deque([beginWord])
        self.dictionary = set()

        for word in wordList:
            self.dictionary.add(word)

        while queue:
            count += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == endWord:
                    return count

                if current in visited:
                    continue

                visited.add(current)
                nextWords = self.getNextWord(current)

                for word in nextWords:
                    queue.append(word)

        return 0

    def getNextWord(self, current):
        results = []
        alpha = "abcdefghijklmnopqrstuvwxyz"

        for idx in range(len(current)):
            for letter in alpha:
                newWord = current[:idx] + letter + current[idx + 1:]

                if newWord in self.dictionary:
                    results.append(newWord)
        return results


# @lc code=end
# "hit"
# "cog"
# ["hot", "dot","dog","lot","log"]

# "hit"
# "cog"
# ["hot", "dot", "dog", "lot", "log", "cog"]
