# https://leetcode.com/problems/long-pressed-name

# two pointers

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        m = len(typed)
        i = j = 0

        while i < n or j < m:
            if i < n and j < m and name[i] == typed[j]:
                i += 1
                j += 1
            elif i > 0 and j < m and name[i-1] == typed[j]:
                j += 1
            else:
                return False

        return i == n and j == m
    
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        m = len(typed)
        i = 0

        for j in range(m):
            if i < n and typed[j] == name[i]:
                i += 1
            elif i > 0 and typed[j] == name[i-1]:
                continue
            else:
                return False
        
        return i == n
