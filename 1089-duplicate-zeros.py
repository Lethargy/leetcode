# https://leetcode.com/problems/duplicate-zeros

from typing import List

# two pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)

        i = n-1
        j = i + arr.count(0)

        while i >= 0:
            if j < n:
                arr[j] = arr[i]

            if arr[i] == 0:
                if j <= n:
                    arr[j-1] = 0
                j -= 2
                i -= 1
            else:
                j -= 1
                i -= 1

# using insert

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0

        while i < n:
            if arr[i] != 0:
                i += 1
            else:
                arr.insert(i,0)
                i += 2
                arr.pop()

        return arr
        
        
