class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        def collapse(stack):
            while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:
                good = stack.pop()
                
                if -good > stack[-1]:
                    _ = stack.pop()
                    stack.append(good)
                elif -good == stack[-1]:
                    _ = stack.pop()

        for num in asteroids:
            stack += [num]
            collapse(stack)
        return stack