# https://leetcode.com/problems/long-pressed-name

# two pointers
    
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        m = len(typed)

        i = j = 0

        while i < n and j < m:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif i > 0 and name[i-1] == typed[j]:
                j += 1
            else:
                return False

        while j < m:
            if name[i-1] == typed[j]:
                j += 1
            else:
                return False

        return i == n and j == m


