# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores

from typing import List

# sliding window

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = k-1
        ans = float('inf')

        while j < len(nums):
            ans = min(ans, nums[j] - nums[i])
            i = i + 1
            j = j + 1
        
        return ans



        