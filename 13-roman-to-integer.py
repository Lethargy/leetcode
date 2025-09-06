# https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
        biggest = s[-1]
        ans = 0

        for c in reversed(s):
            if values[c] >= values[biggest]:
                ans = ans + values[c]
                biggest = c
            else:
                ans = ans - values[c]
        
        return ans