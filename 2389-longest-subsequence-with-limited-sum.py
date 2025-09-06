# https://leetcode.com/problems/longest-subsequence-with-limited-sum

from typing import List
from bisect import bisect_right

# binary search

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        nums.sort()

        for i in range(1,n):
            nums[i] = nums[i] + nums[i-1] # cumulative sum
        
        return [bisect_right(nums,queries[i]) for i in range(m)]
