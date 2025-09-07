# https://leetcode.com/problems/calculate-money-in-leetcode-bank

class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0

        for day in range(n):
            res += 1 + (day % 7) + (day // 7)
        
        return res