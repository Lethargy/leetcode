# https://leetcode.com/problems/count-prefixes-of-a-given-string

from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0

        for w in words:
            if s.startswith(w):
                ans = ans + 1
        
        return ans
    
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:       
        return sum(w == s[:len(w)] for w in words)