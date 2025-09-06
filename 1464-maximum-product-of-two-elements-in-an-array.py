# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array

from typing import List
from heapq import nlargest

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a,b = nlargest(2,nums)
        return (a-1)*(b-1)