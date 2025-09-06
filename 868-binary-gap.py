# https://leetcode.com/problems/binary-gap/submissions

class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        last = float('inf')

        i = 0
        while n > 0:
            n,r = n//2, n%2
            if r == 1:
                ans = max(ans, i - last)
                last = i
            i = i + 1

        return ans
        