# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array

from typing import List

# using nlargest

from heapq import nlargest

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a,b = nlargest(2,nums)
        return (a-1)*(b-1)
    
# using heappush, heappop
    
from heapq import heappush, heappop
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pq = []

        for num in nums:
            heappush(pq, num)
            if len(pq) > 2:
                heappop(pq)

        return (pq[0] - 1) * (pq[1] - 1)