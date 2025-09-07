# https://leetcode.com/problems/number-of-valid-words-in-a-sentence

class Solution:
    def countValidWords(self, sentence: str) -> int:
        res = 0
        words = sentence.split()

        for word in words:
            if any(d in word for d in '0123456789'):
                continue

            if word.count('-') > 1 or word[0] == '-' or word[-1] == '-':
                continue
            
            if '-' in word:
                i = word.index('-')
                if not word[i-1].isalpha() or not word[i+1].isalpha():
                    continue
            
            if word.count('!') + word.count('.') + word.count(',') > 1:
                continue
            
            if any(word.count(p) == 1 and word[-1] != p for p in '!.,'):
                continue

            res += 1

        return res
