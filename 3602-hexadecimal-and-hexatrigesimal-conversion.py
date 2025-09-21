# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion

import string

class Solution:
    def concatHex36(self, n: int) -> str:
        d = '0123456789' + string.ascii_uppercase

        res = ''
        N = n**3
        while N > 0:
            res += d[N%36]
            N //= 36
        
        N = n**2
        while N > 0:
            res += d[N%16]
            N //= 16

        return res[::-1]