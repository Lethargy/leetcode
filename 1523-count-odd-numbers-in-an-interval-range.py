# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1

        return 1 + (high-low)//2