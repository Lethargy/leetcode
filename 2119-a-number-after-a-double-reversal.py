# https://leetcode.com/problems/a-number-after-a-double-reversal

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        else:
            return num % 10 != 0