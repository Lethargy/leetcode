# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter

class Solution:
    def minTimeToType(self, word: str) -> int:
        pos = 'a'
        res = 0

        for c in word:
            res += min((ord(c)-ord(pos)) % 26, (ord(pos) - ord(c)) % 26)
            pos = c
        
        return len(word) + res
