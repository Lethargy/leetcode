# https://leetcode.com/problems/coupon-code-validator

from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid = {'electronics':[], 'grocery':[], 'pharmacy':[], 'restaurant':[]}
        n = len(code)

        for i in range(n):
            if len(code[i]) == 0:
                continue

            if not all(ch.isalnum() or ch == '_' for ch in code[i]):
                continue
            
            if businessLine[i] not in valid:
                continue
            
            if not isActive[i]:
                continue
            
            valid[businessLine[i]].append(code[i])
        
        res = []
        for L in valid.values():
            L.sort()
            res += L

        return res
