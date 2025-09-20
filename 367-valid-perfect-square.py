# https://leetcode.com/problems/valid-perfect-square

# binary search

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        a = 0
        b = num

        while b-a > 1:
            m = (a+b) // 2
            if m**2 <= num < (m+1)**2:
                break
            elif num < m**2:
                b = m
            elif num >= (m+1)**2:
                a = m

        return m**2 == num