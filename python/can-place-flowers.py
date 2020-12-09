class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        for i in range(length):
            left = 0 if i - 1 < 0 else flowerbed[i - 1]
            right = 0 if i + 1 >= length else flowerbed[i + 1]
            if left == 0 and right == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0
