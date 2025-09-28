# https://leetcode.com/problems/perfect-number

from math import isqrt

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        s = 1
        for k in range(2,1+isqrt(num)):
            if num % k == 0:
                s += k
                s += num//k

        return s == num