# https://leetcode.com/problems/maximum-repeating-substring

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0
        while res * word in sequence:
            res += 1

        return res-1