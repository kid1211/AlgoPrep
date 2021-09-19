class Solution {
    func minMeetingRooms(_ intervals: [[Int]]) -> Int {
        var temp = Array<(Int, Int)>()
        
        for item in intervals {
            temp += [(item[0], +1)]
            temp += [(item[1], -1)]
        }
        
        temp = temp.sorted { 
            $0.0 == $1.0 ? $0.1 < $1.1 : $0.0 < $1.0
        }
        print(temp)
        var res = 0, curr = 0
        
        for item in temp {
            curr += item.1
            res = max(res, curr)
        }
        
        return res
    }
}