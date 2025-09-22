# https://leetcode.com/problems/count-tested-devices-after-test-operations

from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0

        for p in batteryPercentages:
            if p > ans:
                ans += 1
        
        return ans