# https://leetcode.com/problems/count-the-number-of-special-characters-i

# hash table

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()

        for ch in word:
            if ch.islower():
                lower.add(ch)
            else:
                upper.add(ch.lower())

        return len(lower & upper)

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [False] * 26
        upper = [False] * 26

        for ch in word:
            if ch.islower():
                lower[ord(ch) - 97] = True
            else:
                upper[ord(ch) - 65] = True
        
        ans = 0
        for i in range(26):
            if lower[i] and upper[i]:
                ans = ans + 1
        
        return ans