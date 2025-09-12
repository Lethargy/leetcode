# https://leetcode.com/problems/sort-vowels-in-a-string

# using counter / hash map (memory efficient but slow)

from collections import Counter

class Solution:
    def sortVowels(self, s: str) -> str:
        vowelCount = Counter(c for c in s if c in 'AEIOUaeiou')
        vowels = sorted(list(vowelCount.keys()), key = ord)
        
        res = ''
        i = 0
        for c in s:
            if c in vowels:
                if vowelCount[vowels[i]] == 0:
                    i += 1
                res += vowels[i]
                vowelCount[vowels[i]] -= 1
            else:
                res += c
        
        return res
    
# using stack (fast but memory inefficient)

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [c for c in s if c in 'AEIOUaeiou']
        vowels.sort(key = ord, reverse = True)

        res = list(s)
        for i,c in enumerate(s):
            if c in 'AEIOUaeiou':
                res[i] = vowels.pop()
        
        return ''.join(res)