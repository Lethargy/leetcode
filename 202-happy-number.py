# https://leetcode.com/problems/happy-number

# hash table

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def nextNum(n):
            out = 0
            while n > 0:
                n,r = n//10, n%10
                out += r**2
            return out

        seen = {n}
        n = nextNum(n)

        while n not in seen:
            seen.add(n)
            n = nextNum(n)

        return n == 1