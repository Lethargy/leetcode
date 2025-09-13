# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array

from typing import List

# using sets

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        n = len(nums)
        limits = set(range(n))

        for i in range(n):
            if nums[i] == key:
                res |= set(range(i-k,i+k+1)) & limits

        return sorted(list(res))
    
# two pointers (faster)
    
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        n = len(nums)
        j = 0

        for i in range(n):
            if nums[i] == key:
                j = max(j, i-k)
                while j < n and j <= i+k:
                    res.append(j)
                    j += 1
                
        return res
