# https://leetcode.com/problems/prime-in-diagonal

from typing import List
from math import isqrt

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(num):
            if num == 1:
                return False
            elif num == 2 or num == 3:
                return True
            
            for k in range(2, isqrt(num)+1):
                if num % k == 0:
                    return False
            
            return True
        
        n = len(nums)
        ans = 0
        
        for i in range(n):
            if isPrime(nums[i][i]):
                ans = max(ans, nums[i][i])
            if isPrime(nums[~i][i]):
                ans = max(ans, nums[~i][i])

        return ans

