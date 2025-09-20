# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations

from typing import List

# using heap
from heapq import heapify, heappush, heappop

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapify(nums)

        while k > 0:
            if nums[0] < 0:
                heappush(nums, -heappop(nums))
                k -= 1
            elif nums[0] == 0 or k % 2 == 0:
                break
            else:
                heappush(nums, -heappop(nums))
                break

        return sum(nums)