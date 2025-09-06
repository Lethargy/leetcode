# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal

from collections import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        dif = 0
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                dif += 1
        
        return Counter(s1) == Counter(s2) and (dif == 2 or dif == 0)
    
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        dif = []
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                dif.append(i)
        
        if len(dif) == 0:
            return True
        
        if len(dif) != 2:
            return False

        if s1[dif[0]] == s2[dif[1]] and s2[dif[0]] == s1[dif[1]]:
            return True
        
        return False