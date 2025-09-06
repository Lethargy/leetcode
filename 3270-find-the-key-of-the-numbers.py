# https://leetcode.com/problems/find-the-key-of-the-numbers

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ans = 0

        for k in range(4):
            ans = ans + 10**k * min(num1 % 10, num2 % 10, num3 % 10)
            num1 = num1 // 10
            num2 = num2 // 10
            num3 = num3 // 10
        
        return ans