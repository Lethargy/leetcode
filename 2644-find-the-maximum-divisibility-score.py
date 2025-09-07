# https://leetcode.com/problems/find-the-maximum-divisibility-score

from typing import List
from math import inf

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res = inf
        best = -inf

        for d in divisors:
            count = 0
            for n in nums:
                if n % d == 0:
                    count += 1
            if count > best:
                res = d
                best = count
            elif count == best:
                res = min(res, d)

        return res