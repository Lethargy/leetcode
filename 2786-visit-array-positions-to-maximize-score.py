# https://leetcode.com/problems/visit-array-positions-to-maximize-score

from typing import List

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)

        def v(i):
            if i == n-1:
                return nums[-1]

            return nums[i] + max(0, max(v(j) - x * abs((nums[j] - nums[i]) % 2) for j in range(i+1,n)))

        return v(0)
    
    
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        v = [None] * n
        v[-1] = nums[-1]

        for i in reversed(range(n-1)):
            v[i] = nums[i] + max(0, max(v[j] - x * abs((nums[j] - nums[i]) % 2) for j in range(i+1,n)))

        return v[0]
    

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        v = nums[-1]

        if nums[-1] % 2 == 0:
            E = v
            O = max(0, v - x)
        else:
            E = max(0, v - x)
            O = v

        for i in reversed(range(n-1)):
            if nums[i] % 2 == 0:
                v = nums[i] + E
                E = max(E, v)
                O = max(O, v - x)
            else:
                v = nums[i] + O
                E = max(E, v - x)
                O = max(O, v)

        return v