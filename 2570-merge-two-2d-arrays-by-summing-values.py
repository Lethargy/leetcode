# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values

from typing import List

# two pointers

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        n1 = len(nums1)
        n2 = len(nums2)

        i = 0
        j = 0

        while i < n1 or j < n2:
            if i == n1:
                res.append(nums2[j])
                j += 1
            elif j == n2:
                res.append(nums1[i])
                i += 1
            elif nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        return res
                    
                    