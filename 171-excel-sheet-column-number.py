# https://leetcode.com/problems/excel-sheet-column-number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        i = 0
        for c in reversed(columnTitle):
            ans = ans + 26**i * (ord(c) - 64)
            i = i + 1

        return ans