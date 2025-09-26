# https://leetcode.com/problems/minimum-cost-to-reach-every-position

from typing import List
from math import inf

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)  
        runMin = inf

        for i in range(n):
            cost[i] = min(runMin, cost[i])
            runMin = min(runMin, cost[i])
        
        return cost
    
# using built-in python tools
    
from itertools import accumulate

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:        
        return list(accumulate(cost, min))