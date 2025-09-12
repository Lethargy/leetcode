# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        res = 0
        y = x
        while y > 0:
            res = 10 * res + (y%10)
            y = y//10
        
        return res == x

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]