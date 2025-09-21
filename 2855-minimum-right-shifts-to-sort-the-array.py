# https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array

from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        count = 0
        start = 0
        n = len(nums)

        for i in range(n):
            if nums[(i+1)%n] < nums[i]:
                count += 1
                start = (i+1)%n
            
        if count > 1:
            return -1
        else:
            return (n - start) % n
            