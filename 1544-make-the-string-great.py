# https://leetcode.com/problems/make-the-string-great

class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]

        for ch in s[1:]:
            if stack and stack[-1].lower() == ch.lower() and stack[-1].islower() != ch.islower():
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)