# https://leetcode.com/problems/count-operations-to-obtain-zero

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while min(num1,num2) > 0:
            if num1 >= num2:
                m = num1 // num2
                num1 -= m * num2
            else:
                m = num2 // num1
                num2 -= m * num1
            ans += m
        return ans
