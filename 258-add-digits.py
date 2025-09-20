# https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            newNum = 0
            while num > 0:
                newNum += num % 10
                num //= 10
            num = newNum
        return num