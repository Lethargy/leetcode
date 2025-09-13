# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant

from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        maxVowelFreq = 0
        maxConsonantFreq = 0
        
        for letter,count in Counter(s).items():
            if letter in 'aeiou':
                maxVowelFreq = max(maxVowelFreq, count)
            else:
                maxConsonantFreq = max(maxConsonantFreq, count)
        
        return maxVowelFreq + maxConsonantFreq
