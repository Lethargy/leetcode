# https://leetcode.com/problems/vowels-of-all-substrings

from typing import List
from functools import cache

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)

        @cache
        def v(i):
            if i == n-1:
                return int(word[i] in 'aeiou')
            elif word[i] in 'aeiou':
                return v(i+1) + n - i
            else:
                return v(i+1)
            
        return sum(v(i) for i in range(n))
    


class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        v = int(word[n-1] in 'aeiou')
        ans = v

        for i in reversed(range(n-1)):
            if word[i] in 'aeiou':
                v = v + n-i
            ans = ans + v
            
        return ans