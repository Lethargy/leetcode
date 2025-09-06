# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''

        for ch in s:
            if ch.isalnum():
                t = t + ch.lower()
        return t == t[::-1]