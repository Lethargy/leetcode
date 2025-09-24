# https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        n = len(word1)
        m = len(word2)

        i = j = 0

        while i < n and j < m:
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1
        
        while i < n:
            ans += word1[i]
            i += 1
        
        while j < m:
            ans += word2[j]
            j += 1

        return ans