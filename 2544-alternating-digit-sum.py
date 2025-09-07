# https://leetcode.com/problems/alternating-digit-sum

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        for i,d in enumerate(str(n)):
            res += (-1)**(i) * int(d)
        return res
    
# pythonic

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum((-1)**(i) * int(d) for i,d in enumerate(str(n)))