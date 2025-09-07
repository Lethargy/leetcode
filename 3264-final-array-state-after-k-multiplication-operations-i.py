# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i

from typing import List
from heapq import heappush, heappop

# priority queue

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = [] # priority queue

        for i,num in enumerate(nums):
            heappush(pq, (num,i))
        
        for _ in range(k):
            num,i = heappop(pq)
            num *= multiplier
            heappush(pq,(num,i))
        
        for num,i in pq:
            nums[i] = num
        
        return nums