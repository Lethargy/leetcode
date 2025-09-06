# https://leetcode.com/problems/sqrtx

# binary search

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1

        a = 0
        b = x

        while b-a > 1:
            m = (a+b) // 2
            if m**2 <= x < (m+1)**2:
                return m
            elif x < m**2:
                b = m
            elif x >= (m+1)**2:
                a = m
                
# built-in

class Solution:
    def mySqrt(self, x: int) -> int:
        return bisect_right(range(x+1), x, key = lambda x: x**2) - 1