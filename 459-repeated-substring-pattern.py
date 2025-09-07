# https://leetcode.com/problems/repeated-substring-pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(1,n//2+1):
            if s[:i] * (n//i) == s:
                return True
        
        return False

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:        
        return s in (s + s)[1:-1]