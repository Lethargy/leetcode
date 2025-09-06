# https://leetcode.com/problems/faulty-keyboard

class Solution:
    def finalString(self, s: str) -> str:
        ans = ''
        
        for ch in s:
            if ch == 'i':
                ans = ans[::-1]
            else:
                ans = ans + ch

        return ans