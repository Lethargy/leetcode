# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h1,m1 = current.split(':')
        h2,m2 = correct.split(':')

        diff = 60*int(h2) + int(m2) - 60*int(h1) - int(m1)
        ans = 0
        
        for m in [60,15,5,1]:
            ans += diff // m
            diff %= m

        return ans