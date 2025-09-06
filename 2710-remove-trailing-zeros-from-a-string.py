# https://leetcode.com/problems/remove-trailing-zeros-from-a-string

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i = len(num) - 1

        while num[i] == '0':
            i = i - 1
        
        return num[:i+1]
        
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')
        