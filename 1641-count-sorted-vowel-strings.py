# https://leetcode.com/problems/count-sorted-vowel-strings

from functools import cache

class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def v(k,n):
            if n == 1:
                return k

            if k == 1:
                return 1

            return v(k,n-1) + v(k-1,n)

        return v(5,n)