# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array

from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        
        for i in range(n):
            ans = max(ans, abs(nums[(i+1)%n]-nums[i]))

        return ans