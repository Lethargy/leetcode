# https://leetcode.com/problems/minimum-moves-to-convert-string

# first attempt

# O(n) time, O(1) space

class Solution:
    def minimumMoves(self, s: str) -> int:
        res = 0
        i = 0
        n = len(s)

        while i < n:
            while i < n and s[i] != 'X':
                i += 1
            
            if i < n:
                res += 1
                i += 3

        return res

# improved

class Solution:
    def minimumMoves(self, s: str) -> int:
        res = 0
        i = 0

        while i < len(s):
            if s[i] == 'O':
                i += 1
            else:
                res += 1
                i += 3

        return res