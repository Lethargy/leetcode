# https://leetcode.com/problems/reformat-the-string

class Solution:
    def reformat(self, s: str) -> str:
        A = [ch for ch in s if ch.isalpha()]
        D = [ch for ch in s if ch.isnumeric()]

        if abs(len(A) - len(D)) > 1:
            return ''

        if len(D) > len(A):
            A,D = D,A

        ans = ''
        i = 0
        while A or D:
            if i % 2 == 0:
                ans = ans + A.pop()
            else:
                ans = ans + D.pop()
            i = i + 1

        return ans