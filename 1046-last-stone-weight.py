# https://leetcode.com/problems/last-stone-weight

from typing import List
from heapq import heappop, heappush, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)

        while len(stones) >= 2:
            y = heappop(stones)
            x = heappop(stones)
            
            if y < x:
                heappush(stones, y-x)
        
        return -stones[0] if stones else 0