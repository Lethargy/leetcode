# https://leetcode.com/problems/contains-duplicate-ii

from typing import List

# sliding window

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i = 0
        seen = set()

        for j in range(n):
            while j-i > k:
                seen.remove(nums[i])
                i += 1

            if nums[j] in seen:
                return True
            
            seen.add(nums[j])
        
        return False

        