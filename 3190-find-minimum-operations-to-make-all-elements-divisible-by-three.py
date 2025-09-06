# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans = ans + int(num % 3 != 0)
        
        return ans