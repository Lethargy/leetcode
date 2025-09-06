# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity

from heapq import heappush, heappop

# sorting

class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        odd = []
        isEven = []

        while num > 0:
            num, rem = num // 10, num % 10
            if rem % 2 == 0:
                even.append(rem)
                isEven.append(True)
            else:
                odd.append(rem)
                isEven.append(False)

        even.sort()
        odd.sort()

        ans = 0
        for b in reversed(isEven):
            if b:
                ans = 10 * ans + even.pop()
            else:
                ans = 10 * ans + odd.pop()
        
        return ans

# priority queue

class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        odd = []
        isEven = []

        while num > 0:
            num, rem = num // 10, num % 10
            if rem % 2 == 0:
                heappush(even, -rem)
                isEven.append(True)
            else:
                heappush(odd, -rem)
                isEven.append(False)

        ans = 0
        for b in reversed(isEven):
            if b:
                ans = 10 * ans - heappop(even)
            else:
                ans = 10 * ans - heappop(odd)
        
        return ans

        
        