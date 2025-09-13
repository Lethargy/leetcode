# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i

from typing import List

# greedy

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        b = None

        for i,g in enumerate(groups):
            if g != b:
                res.append(words[i])
                b = g
        
        return res