# https://leetcode.com/problems/find-the-pivot-integer

# prefix sum
# O(n) time, O(1) space

class Solution:
    def pivotInteger(self, n: int) -> int:
        S = n * (n+1) // 2

        prefixSum = x = 1
        while prefixSum < S - prefixSum + x:
            x += 1
            prefixSum += x

        if prefixSum == S - prefixSum + x:
            return x
        else:
            return -1

# math
# O(1) time, O(1) space

from math import isqrt

class Solution:
    def pivotInteger(self, n: int) -> int:
        x2 = (n**2+n) // 2
        x = isqrt(x2)

        if x**2 == x2:
            return x
        else:
            return -1