# https://leetcode.com/problems/reverse-vowels-of-a-string

# two pointers

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i = 0
        j = n - 1
        vowels = {'a','e','i','o','u','A','E','I','O','U'}

        while i < j:
            while s[i] not in vowels and i < j:
                i = i + 1
            while s[j] not in vowels and i < j:
                j = j - 1
            s[i], s[j] = s[j], s[i]
            i = i + 1
            j = j - 1
        
        return ''.join(s)
