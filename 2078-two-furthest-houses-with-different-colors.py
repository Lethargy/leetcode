# https://leetcode.com/problems/two-furthest-houses-with-different-colors

from typing import List

# greedy

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i = 0
        j = n - 1

        while colors[i] == colors[n-1]:
            i = i + 1
        while colors[0] == colors[j]:
            j = j - 1

        return max(j, n-1-i)