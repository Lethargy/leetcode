# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def value(s):
            out = 0
            for ch in s:
                out *= 10
                out += ord(ch) - ord('a')
            return out
        
        return value(firstWord) + value(secondWord) == value(targetWord)