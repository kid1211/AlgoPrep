// should use heap
class Solution {
    func kClosest(_ points: [[Int]], _ k: Int) -> [[Int]] {
        var distToPoint = [Double: [[Int]]]()
        
        for pt in points {
            let distance = sqrt(Double(pt[0] * pt[0]) + Double(pt[1] * pt[1]))
            
            if distToPoint[distance] == nil {
                distToPoint[distance] = [pt]
            } else {
                distToPoint[distance]! += [pt]
            }
        }
        
        var sortingKeys = distToPoint.keys.sorted()
        var res:[[Int]] = []
        let total = points.count
        
        for key in sortingKeys {
            for val in distToPoint[key]! {
                res += [val]
                
                if res.count >= k {
                    return res
                }
            }
        }
        
        return res
    }
}