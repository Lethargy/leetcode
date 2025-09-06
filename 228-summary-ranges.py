# https://leetcode.com/problems/summary-ranges

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        start = nums[0]
        prev = nums[0]
        nums.append(None)

        for num in nums[1:]:
            if num != prev + 1:
                if prev == start:
                    ans.append(str(prev))
                else:
                    ans.append(str(start) + '->' + str(prev))
                start = num
            prev = num
        
        return ans


