# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array

from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ''

        for word in words:
            prefix += word
            if prefix == s:
                return True
        
        return False