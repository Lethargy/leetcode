# https://leetcode.com/problems/merge-sorted-array/description

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        p = n+m-1

        while i >= 0 or j >= 0:
            if i < 0:
                nums1[p], nums2[j] = nums2[j], nums1[p]
                j -= 1
                p -=1
            elif j < 0:
                nums1[p], nums1[i] = nums1[i], nums1[p]
                i -= 1
                p -=1
            elif nums1[i] >= nums2[j]:
                nums1[p], nums1[i] = nums1[i], nums1[p]
                i -= 1
                p -=1
            elif nums1[i] < nums2[j]:
                nums1[p], nums2[j] = nums2[j], nums1[p]
                j -= 1
                p -=1