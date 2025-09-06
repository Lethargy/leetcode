# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i

class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(set(word))

        ans = 0
        k = 1
        while n > 0:
            ans = ans + k * min(8, n)
            n = n - 8
            k = k + 1
        
        return ans