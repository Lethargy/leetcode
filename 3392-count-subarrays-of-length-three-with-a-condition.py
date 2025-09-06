# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(n-2):
            if 2*(nums[i] + nums[i+2]) == nums[i+1]:
                res += 1

        return res
        