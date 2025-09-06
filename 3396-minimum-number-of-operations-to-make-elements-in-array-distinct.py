# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct

from typing import List

# hash table

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        n = len(nums)

        for i in reversed(range(n)):
            if nums[i] in seen:
                return 1 + i//3 # ceil((i+1)/3)
            else:
                seen.add(nums[i])
        
        return 0

        
        