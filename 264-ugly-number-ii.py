# https://leetcode.com/problems/ugly-number-ii

from heapq import heappop, heappush

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        k = 1
        pq = [2,3,5]
        
        while k < n:
            a = heappop(pq)
            if a == ans:
                continue
            heappush(pq, 2*a)
            heappush(pq, 3*a)
            heappush(pq, 5*a)

            ans = a
            k = k + 1
        return ans
    
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        primes = [2,3,5]
        pq = [(p,p) for p in primes]
        
        for _ in range(n-1):
            a, p0 = heappop(pq)

            for p in primes:
                if p <= p0:
                    heappush(pq, (p*a,p))
            ans = a
        return ans