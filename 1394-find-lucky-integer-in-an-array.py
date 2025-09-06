# https://leetcode.com/problems/find-lucky-integer-in-an-array

from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)

        ans = -1
        for num,freq in count.items():
            if num == freq:
                ans = max(ans, num)
        
        return ans