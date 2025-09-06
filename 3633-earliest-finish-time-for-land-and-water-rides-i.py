# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i

from typing import List

# greedy

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float('inf')
        n = len(landStartTime)
        m = len(waterStartTime)
        
        # land first
        t = float('inf')
        for i in range(n):
            t = min(t, landStartTime[i] + landDuration[i])
        
        for j in range(m):
            res = min(res, max(t, waterStartTime[j]) + waterDuration[j])

        # water first
        t = float('inf')
        for j in range(m):
            t = min(t, waterStartTime[j] + waterDuration[j])
        
        for i in range(n):
            res = min(res, max(t, landStartTime[i]) + landDuration[i])

        return res