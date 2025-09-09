# https://leetcode.com/problems/next-greater-element-i

from typing import List

# monotonic stack

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = dict()
        stack = []

        for num in reversed(nums2):
            while stack and stack[-1] < num:
                stack.pop()
            
            if stack:
                nextGreater[num] = stack[-1]
            
            stack.append(num)
        
        res = [-1] * len(nums1)
        for i,num in enumerate(nums1):
            if num in nextGreater:
                res[i] = nextGreater[num]

        return res





