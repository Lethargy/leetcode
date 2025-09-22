# https://leetcode.com/problems/count-good-triplets

from typing import List
from itertools import combinations

# O(n^3) time, O(1) space

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        n = len(arr)
        for i,j,k in combinations(range(n),3):
            if abs(arr[i]-arr[j]) > a:
                continue
            elif abs(arr[j]-arr[k]) > b:
                continue
            elif abs(arr[i]-arr[k]) > c:
                continue
            ans += 1
        
        return ans
        