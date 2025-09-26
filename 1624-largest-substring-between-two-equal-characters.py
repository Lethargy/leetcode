# https://leetcode.com/problems/largest-substring-between-two-equal-characters

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = dict()
        ans = -1

        for i,c in enumerate(s):
            if c in seen:
                ans = max(ans, i - seen[c] - 1)
            else:
                seen[c] = i
        
        return ans