# https://leetcode.com/problems/third-maximum-number

from typing import List
from heapq import heappush, heappop

# priority queue

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        pq = []
        seen = set()

        for num in nums:
            if num not in seen:
                heappush(pq,num)
                seen.add(num)
            if len(pq) > 3:
                heappop(pq)
        
        if len(pq) < 3:
            return max(pq)
        else:
            return heappop(pq)
        
        
