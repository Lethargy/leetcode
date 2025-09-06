# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i

from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        maxOdd = -float('inf')
        minEven = float('inf')

        for n in count.values():
            if n % 2 == 0:
                minEven = min(minEven, n)
            else:
                maxOdd = max(maxOdd, n)
        
        return maxOdd - minEven