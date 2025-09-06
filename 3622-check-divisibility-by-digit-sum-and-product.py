# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        p = 1
        s = 0
        N = n
        while N > 0:
            N,r = N//10,N%10
            p *= r
            s += r
        
        return (p+s) * (n // (p+s)) == n
        