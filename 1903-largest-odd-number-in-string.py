# https://leetcode.com/problems/largest-odd-number-in-string

class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        oddDigits = {'1', '3', '5', '7', '9'}

        while i >= 0 and num[i] not in oddDigits:
            i -= 1
        
        return num[:i+1]
