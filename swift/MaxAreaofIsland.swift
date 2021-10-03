class Solution {
    var visited = Set<Double>()
    var size = 0
    
    func hashCoordinate(_ coor: (Int, Int)) -> Double {
        let (X, Y) = coor
        return Double(X) * 1723.0 + Double(Y) * 213.0;
    }
    
    func maxAreaOfIsland(_ grid: [[Int]]) -> Int {
        var maxIslandSize = 0
        
        for row in 0..<grid.count {
            for col in 0..<grid[row].count {
                if grid[row][col] == 0 { continue }
                let coord = (row, col)
                if visited.contains(hashCoordinate(coord)) { continue }
                visited.insert(hashCoordinate(coord))
                size = 1
                dfs(coord, grid)
                maxIslandSize = max(maxIslandSize, size)
            }
        }
        
        return maxIslandSize
    }
    
    func dfs(_ coord: (Int, Int), _ grid: [[Int]]) {
        // print(coord)
        func islandValid(_ coor: (Int, Int)) -> Bool {
            let (X, Y) = coor
            
            if X < 0 || X >= grid.count { return false }
            if Y < 0 || Y >= grid[X].count { return false }
            
            return grid[X][Y] == 1
        }
    
        for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)] {
            let (dx, dy) = delta
            let (x, y) = coord
            let nextC = (dx + x, dy + y)
            
            
            if islandValid(nextC) {
                if visited.contains(hashCoordinate(nextC)) { continue }
                visited.insert(hashCoordinate(nextC))
                size += 1
                dfs(nextC, grid)
            }
        }
        
        return 
    }
}