# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams

from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        sortedWords = [''.join(sorted(word)) for word in words]

        ans = []
        n = len(words)

        i = j = 0
        while j < n:
            if sortedWords[i] == sortedWords[j]:
                j += 1
            else:
                ans.append(words[i])
                i = j
        
        ans.append(words[i])
        return ans