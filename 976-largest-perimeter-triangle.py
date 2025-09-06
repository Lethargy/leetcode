# https://leetcode.com/problems/largest-perimeter-triangle

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = n-3
        j = n-2
        k = n-1

        while nums[i] + nums[j] <= nums[k] and i >= 0:
            i = i - 1
            j = j - 1
            k = k - 1
        
        if i < 0:
            return 0
        else:
            return nums[i] + nums[j] + nums[k]