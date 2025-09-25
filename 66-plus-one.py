# https://leetcode.com/problems/plus-one

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []

        for i,d in enumerate(reversed(digits)):
            if i == 0:
                ans.append((d+1)%10)
                c = (d+1)//10
            else:
                ans.append((c+d)%10)
                c = (c+d)//10
        
        if c: ans.append(c)

        return list(reversed(ans))