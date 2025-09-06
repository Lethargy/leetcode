# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k

from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        ans = []

        for i in range(0,n,k):
            if i+k <= n:
                ans.append(s[i:i+k])
            else:
                ans.append(s[i:] + fill * (k - len(s[i:])))
            
        return ans