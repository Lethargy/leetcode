# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum

from functools import cache
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)

        @cache
        def even(i): # number of even sum subarrays starting at arr[i]
            if i == n-1:
                if arr[i] % 2 == 0:
                    return 1
                else:
                    return 0
            
            if arr[i] % 2 == 0:
                return 1 + even(i+1)
            
            if arr[i] % 2 == 1:
                return odd(i+1)

        @cache
        def odd(i): # number of odd sum subarrays starting at arr[i]
            if i == n-1:
                if arr[i] % 2 == 1:
                    return 1
                else:
                    return 0

            if arr[i] % 2 == 0:
                return odd(i+1)
            
            if arr[i] % 2 == 1:
                return 1 + even(i+1)
        
        return sum(odd(i) for i in range(n)) % (10**9 + 7)
    
# tabulated; O(n) complexity, O(1) space

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)

        if arr[n-1] % 2 == 1:
            odd = 1
            even = 0
        else:
            odd = 0
            even = 1

        ans = odd

        for i in reversed(range(n-1)):
            if arr[i] % 2 == 1:
                even, odd = odd, 1 + even
            else:
                even, odd = 1 + even, odd
            
            ans = ans + odd

        return ans % (10**9 + 7)