# https://leetcode.com/problems/replace-non-coprime-numbers-in-array

from typing import List
from math import gcd, lcm

# stack

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            stack.append(num)
            while len(stack) >= 2 and gcd(stack[-1], stack[-2]) != 1:
                stack.append(lcm(stack.pop(), stack.pop()))
        
        return stack