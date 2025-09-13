# https://leetcode.com/problems/complement-of-base-10-integer

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        res = 0
        p = 0
        while n > 0:
            n,r = n//2,n%2
            res += (1-r)*2**p
            p += 1
        
        return res