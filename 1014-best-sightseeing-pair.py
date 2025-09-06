# https://leetcode.com/problems/best-sightseeing-pair

from typing import List
from functools import cache

# VERSON 1: O(n^2) complexity, O(n) memory  

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        @cache
        def s(i): # best score in values[i],...,values[n-1]
            if i == n-2:
                return values[n-2] + values[n-1] - 1
            
            return max(s(i+1), max(values[i] + values[j] + i - j for j in range(i+1,n)))
    
        return s(0)
    
# VERSON 2: O(n) complexity, O(n) memory    

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        @cache
        def s(i):
            if i == n-2:
                return values[n-2] + values[n-1] - 1
            
            return max(s(i+1), values[i] + i + M(i+1))
            
        @cache
        def M(i):
            if i == n-1:
                return values[n-1] - (n-1)

            return max(M(i+1), values[i] - i)
    
        return s(0)
    
# VERSON 3: O(n) complexity, O(n) memory
    
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        s = [None] * (n-1)
        M = [None] * (n-1)

        s[n-2] = values[n-2] + values[n-1] - 1
        M[n-2] = max(values[n-2] - (n-2), values[n-1] - (n-1))

        for i in reversed(range(n-2)):
            s[i] = max(s[i+1], values[i] + i + M[i+1])
            M[i] = max(M[i+1], values[i] - i)

        return s[0]
    
# VERSON 4: O(n) complexity, O(1) memory
    
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        s = values[n-2] + values[n-1] - 1
        M = max(values[n-2] - (n-2), values[n-1] - (n-1))

        for i in reversed(range(n-2)):
            s = max(s, values[i] + i + M)
            M = max(M, values[i] - i)

        return s