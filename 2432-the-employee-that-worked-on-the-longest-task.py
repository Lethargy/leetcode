# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task

from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        res = None
        maxTime = -float('inf')
        last = 0

        for id, leaveTime in logs:
            if leaveTime - last > maxTime:
                maxTime = leaveTime - last
                res = id
            elif leaveTime - last == maxTime:
                res = min(res, id)
            last = leaveTime

        return res