# https://leetcode.com/problems/minimum-cost-for-tickets

from typing import List
from functools import cache
from bisect import bisect_left    
    
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        @cache
        def v(i):
            if i >= n:
                return 0

            d = bisect_left(days, days[i] + 1) # index look-up
            w = bisect_left(days, days[i] + 7)
            m = bisect_left(days, days[i] + 30)

            return min(costs[0] + v(d), costs[1] + v(w), costs[2] + v(m))

        return v(0)