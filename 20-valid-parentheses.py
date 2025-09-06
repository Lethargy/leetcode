# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            for l,r in [('(',')'),('{','}'),('[',']')]:
                if ch == l:
                    stack.append(l)
                if ch == r:
                    if not stack or stack.pop() != l:
                        return False
            
        return not stack