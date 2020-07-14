/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

      public class Solution extends VersionControl {
        // https://leetcode.com/problems/first-bad-version/submissions/
        public int firstBadVersion(int n) {
            int start = 0;
            int end = n;
            int firstBadVersion = -1;
            while(start <= end) {
                int mid = start + (end - start) / 2;
                
                if(isBadVersion(mid)) {
                    firstBadVersion = mid;
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            }
            
            return firstBadVersion;
        }
    }