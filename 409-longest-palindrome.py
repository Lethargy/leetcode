# https://leetcode.com/problems/longest-palindrome

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        
        res = 0
        odd = 0
        for n in count.values():
            if n % 2 == 0:
                res += n
            else:
                odd = 1
                res += n-1
        
        return res + odd
