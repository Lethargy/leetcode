# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        ans = 0

        for word in words:
            if Counter(word) <= chars:
                ans += len(word)
        
        return ans