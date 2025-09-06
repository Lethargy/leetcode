# https://leetcode.com/problems/find-smallest-letter-greater-than-target

from bisect import bisect_right
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target) % len(letters)]

# O(n)

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or letters[-1] <= target:
            return letters[0]

        n = len(letters)

        for i in range(1,n):
            if letters[i-1] <= target < letters[i]:
                return letters[i]

# bisection O(log n)
    
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        j = len(letters) - 1

        if letters[i] > target:
            return letters[i]
        
        if letters[j] <= target:
            return letters[0]

        while j - i > 1:
            m = (i+j) // 2
            if letters[m-1] <= target < letters[m]:
                return letters[m]
            elif target >= letters[m]:
                i = m
            elif letters[m-1] > target:
                j = m
        
        return letters[j]