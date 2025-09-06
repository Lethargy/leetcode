# https://leetcode.com/problems/three-divisors

from math import sqrt

class Solution:
    def isThree(self, n: int) -> bool:
        primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
        s = int(sqrt(n))
        if n != s**2:
            return False

        return s in primes