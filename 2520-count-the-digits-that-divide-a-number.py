# https://leetcode.com/problems/count-the-digits-that-divide-a-number

class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        n = num
        while n > 0:
            n, r = n//10, n%10
            if num % r == 0:
                res += 1
        
        return res
    
# pythonic syntax

class Solution:
    def countDigits(self, num: int) -> int:        
        return sum(num % int(d) == 0 for d in str(num))