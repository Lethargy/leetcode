# https://leetcode.com/problems/min-cost-climbing-stairs

from tpying import List
from functools import cache

# dynamic programming

# Let dp(i) denote our lowest cost starting at stair i.
# We have two options:
# 1. Climb one step. We pay cost[i] and start again from step i+1
#    In this case, our cost becomes cost[i] + dp(i+1)
# 2. Climb two steps. We pay cost[i] and start again from step i+2
#    In this case, our cost becomes cost[i] + dp(i+2)
# We want the smaller of these two:
# dp(i) = min(cost[i] + dp(i+1), cost[i] + dp(i+2))
#       = cost[i] + min(dp(i+1), dp(i+2))
# Boundary conditions: 
# If we are past the last step, we pay nothing: dp(i) = 0, i >= n
# return min(dp(0), dp(1))

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def dp(i):
            if i >= n:
                return 0
            return cost[i] + min(dp(i+1), dp(i+2))

        return min(dp(0),dp(1))
    
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp1 = 0
        dp0 = cost[n-1]

        for i in reversed(range(n-1)):
            dp0, dp1 = cost[i] +  min(dp0,dp1), dp0

        return min(dp0,dp1)



