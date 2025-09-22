# https://leetcode.com/problems/number-of-common-factors

from math import gcd

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0

        for p in range(1,gcd(a,b)+1):
            if a % p == 0 and b % p == 0:
                count += 1
        
        return count