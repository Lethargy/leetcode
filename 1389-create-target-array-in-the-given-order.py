# https://leetcode.com/problems/create-target-array-in-the-given-order

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []

        for num,i in zip(nums,index):
            ans.insert(i,num)

        return ans