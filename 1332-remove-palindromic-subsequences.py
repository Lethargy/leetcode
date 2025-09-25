# https://leetcode.com/problems/remove-palindromic-subsequences

# if s is already a palindrome, return 1
# if s is not a palindrome, first remove all of the a's
# and then all of the b's (2 palindromic substring removals)

# two pointers

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        i = 0
        j = n-1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return 2
        
        return 1