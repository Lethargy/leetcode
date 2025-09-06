# https://leetcode.com/problems/find-the-original-typed-string-i

class Solution:
    def possibleStringCount(self, word: str) -> int:
        word = word + '*'
        ans = 1
        last = word[0]
        streak = 1
        
        for ch in word[1:]:
            if ch == last:
                streak = streak + 1
            else:
                ans = ans + streak - 1
                last = ch
                streak = 1

        return ans
