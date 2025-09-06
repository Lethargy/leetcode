# https://leetcode.com/problems/min-cost-climbing-stairs

from tpying import List
from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def v(i):
            if i >= n:
                return 0
            
            if i == n-1:
                return cost[n-1]

            return min(cost[i] + v(i+1), cost[i] + v(i+2))

        return min(v(0),v(1))
    
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        v = [None] * (n+1)

        v[n] = 0
        v[n-1] = cost[n-1]

        for i in reversed(range(n-1)):
            v[i] = min(cost[i] + v[i+1], cost[i] + v[i+2])

        return min(v[0],v[1])