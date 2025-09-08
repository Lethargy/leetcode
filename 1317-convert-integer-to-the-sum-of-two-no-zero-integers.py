# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers

from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = n
        b = 0
        
        while '0' in str(a) or '0' in str(b):
            a -= 1
            b += 1
        
        return [a,b]