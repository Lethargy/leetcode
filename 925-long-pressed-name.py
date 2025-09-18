# https://leetcode.com/problems/long-pressed-name

# two pointers
    
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        m = len(typed)

        i = j = 0

        while i <= n or j <= m:
            if i == n and j == m:
                return True
            elif j == m:
                return False
            elif i < n and typed[j] == name[i]:
                i += 1
                j += 1
            elif i > 0 and typed[j] == name[i-1]:
                j += 1
            else:
                return False


