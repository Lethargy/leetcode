# https://leetcode.com/problems/find-maximum-number-of-string-pairs

from typing import List

# hash table

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        seen = set()
        for word in words:
            if word[::-1] in seen:
                ans = ans + 1
            else:
                seen.add(word)
    
        return ans