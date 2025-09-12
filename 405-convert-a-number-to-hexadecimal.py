# https://leetcode.com/problems/convert-a-number-to-hexadecimal

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        hexMap = '0123456789abcdef'
        res = []

        if num < 0:
            num += 2**32

        while num > 0:
            num,rem = num//16,num%16
            res.append(hexMap[rem])

        res.reverse()
        return ''.join(res)