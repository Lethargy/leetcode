# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

from collections import Counter

# sliding window

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = 0
        seen = Counter()
        i = 0

        for j,ch in enumerate(s):
            seen[ch] += 1

            while seen[ch] > 2:
                seen[s[i]] -= 1
                i += 1
            
            res = max(res,j-i+1)
        
        return res