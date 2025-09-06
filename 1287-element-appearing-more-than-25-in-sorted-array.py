# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array

from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        j = n//4

        while j < n:
            if arr[i] == arr[j]:
                return arr[i]
            i += 1
            j += 1