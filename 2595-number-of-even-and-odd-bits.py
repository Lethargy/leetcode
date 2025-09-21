# https://leetcode.com/problems/number-of-even-and-odd-bits

from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0,0]

        i = 0
        while n > 0:
            n,r = n //2, n % 2
            ans[i % 2] = ans[i % 2] + r
            i = i + 1
        
        return ans
        