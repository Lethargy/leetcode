# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0

        while n > 0:
            n,r = n//10, n%10
            p = p * r
            s = s + r

        return p - s
        