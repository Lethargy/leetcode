# https://leetcode.com/problems/delete-characters-to-make-fancy-string

class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        prev = None
        count = 0

        for c in s:
            if c == prev:
                count += 1
            else:
                count = 1
                prev = c
            
            if count < 3:
                ans.append(c)
        
        return ''.join(ans)