# https://leetcode.com/problems/number-of-senior-citizens

from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for detail in details:
            if int(detail[11:13]) > 60:
                res += 1
        
        return res