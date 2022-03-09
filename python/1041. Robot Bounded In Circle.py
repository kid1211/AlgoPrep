class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north, east, south, west
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        face = 0 # north
        
        for ins in instructions:
            if ins == 'L':
                face = (face + 3) % 4
            elif ins =='R':
                face = (face + 1) % 4
            else:
                dx, dy = direction[face]
                x += dx
                y += dy
                
        return (x == 0 and y == 0) or face != 0
        