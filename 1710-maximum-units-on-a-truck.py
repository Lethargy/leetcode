# https://leetcode.com/problems/maximum-units-on-a-truck

from typing import List

# priority queue

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1])

        ans = 0
        while truckSize > 0 and boxTypes:
            boxes, units = boxTypes.pop()
            ans = ans + min(boxes,truckSize) * units
            truckSize = truckSize - min(boxes,truckSize)

        return ans