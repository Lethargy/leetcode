# https://leetcode.com/problems/determine-if-string-halves-are-alike

# O(n) time, O(1) space

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)

        firstHalf = 0
        secondHalf = 0

        for i in range(n//2):
            if s[i] in {'a','e','i','o','u','A','E','I','O','U'}:
                firstHalf += 1
        
        for i in range(n//2,n):
            if s[i] in {'a','e','i','o','u','A','E','I','O','U'}:
                secondHalf += 1
        
        return firstHalf == secondHalf