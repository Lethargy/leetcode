# https://leetcode.com/problems/largest-time-for-given-digits 

from typing import List

# greedy

from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        for h1,h2,m1,m2 in permutations(sorted(arr, reverse=True)):
            if (h1,h2) < (2, 4) and m1 < 6:
                return f'{h1}{h2}:{m1}{m2}'
        return ''

# backtracking

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort()

        if arr[0] > 2:
            return ''

        stack = [([],arr)]
        h1 = None
        h2 = None
        m1 = None
        m2 = None
        mins = -float('inf')

        while stack:
            t, rem = stack.pop()
            if len(t) == 1 and t[0] > 2:
                continue

            if len(t) == 2 and t[0] == 2 and t[1] > 3:
                continue

            if len(t) == 3 and t[2] > 5:
                continue

            if len(t) == 4:
                if 60 * (10*t[0] + t[1]) + 10 * t[2] + t[3] > mins:
                    h1 = t[0]
                    h2 = t[1]
                    m1 = t[2]
                    m2 = t[3]
                    mins = 60 * (10*t[0] + t[1]) + 10 * t[2] + t[3]
                continue

            for r in rem:
                copy = rem[:]
                copy.remove(r)
                stack.append((t + [r],copy))
            
        if h1 is None:
            return ''
        else:
            return str(h1) + str(h2) + ':' + str(m1) + str(m2)
