# https://leetcode.com/problems/minimum-bit-flips-to-convert-number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        while start > 0 or goal > 0:
            ans += abs(goal%2 - start%2)
            goal //= 2
            start //= 2

        return ans

# using bit manipulation

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()

