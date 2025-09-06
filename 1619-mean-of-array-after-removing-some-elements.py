# https://leetcode.com/problems/mean-of-array-after-removing-some-elements

from typing import List
from statistics import mean

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        k = len(arr) // 20
        return mean(arr[k:-k])