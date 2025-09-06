# https://leetcode.com/problems/stone-removal-game

class Solution:
    def canAliceWin(self, n: int) -> bool:
        i = 0
        s = 10
        while n >= 0:
            n = n - s
            i = i + 1
            s = s - 1
        
        return i % 2 == 0

        