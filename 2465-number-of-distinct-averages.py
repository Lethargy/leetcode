# https://leetcode.com/problems/number-of-distinct-averages

from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages = set()
        nums.sort()
        i = 0
        j = len(nums)-1

        while i < j:
            averages.add(0.5 * (nums[i] + nums[j]))
            i += 1
            j -= 1
        
        return len(averages)
