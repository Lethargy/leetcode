# https://leetcode.com/problems/super-ugly-number

from heapq import heappop, heappush

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ans = 1
        k = 1
        pq = primes[:]
        
        while k < n:
            a = heappop(pq)
            if a == ans:
                continue
            for p in primes:
                if p*a < 2**31:
                    heappush(pq, p*a)
            ans = a
            k = k + 1
        return ans
    
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ans = 1
        pq = [(p,p) for p in primes]
        
        for _ in range(n-1):
            a,p0 = heappop(pq)

            for p in primes:
                if p*a < 2**31 and p <= p0:
                    heappush(pq, (p*a,p))
            ans = a
        return ans