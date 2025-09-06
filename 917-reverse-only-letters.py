# https://leetcode.com/problems/reverse-only-letters


# set and stack

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        idx = set()
        stack = []

        for i,ch in enumerate(s):
            if ch.isalpha():
                idx.add(i)
                stack.append(ch)
        
        ans = ''
        for i,ch in enumerate(s):
            if i in idx:
                ans = ans + stack.pop()
            else:
                ans = ans + ch

        return ans