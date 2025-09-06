# https://leetcode.com/problems/detect-capital

# manually, by cases

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        if word[0].isupper() and word[1].isupper():
            for ch in word[2:]:
                if not ch.isupper():
                    return False
        
        if not word[0].isupper() and not word[1].isupper():
            for ch in word[2:]:
                if ch.isupper():
                    return False
        
        if word[0].isupper() and not word[1].isupper():
            for ch in word[2:]:
                if ch.isupper():
                    return False

        if not word[0].isupper() and word[1].isupper():
            return False

        return True
    
# built-in
    
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()