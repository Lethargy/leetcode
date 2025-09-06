# https://leetcode.com/problems/maximum-number-of-words-you-can-type

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        ans = len(words)
        for word in text.split():
            for ch in brokenLetters:
                if ch in word:
                    ans = ans - 1
                    break
        
        return ans