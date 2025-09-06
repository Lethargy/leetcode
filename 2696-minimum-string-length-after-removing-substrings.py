# https://leetcode.com/problems/minimum-string-length-after-removing-substrings

# stack

class Solution:
    def minLength(self, s: str) -> int:
        ans = len(s)
        stack = []

        for ch in s:
            if ch == 'A' or ch == 'C':
                stack.append(ch)
            elif ch == 'B' and stack and stack[-1] == 'A':
                stack.pop()
                ans = ans - 2
            elif ch == 'D' and stack and stack[-1] == 'C':
                stack.pop()
                ans = ans - 2
            else:
                stack = []
        
        return ans
        