# https://leetcode.com/problems/sort-even-and-odd-indices-independently/

from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd = []
        even = []

        for i,num in enumerate(nums):
            if i % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        even.sort()
        odd.sort(reverse = True)

        for i in range(n):
            if i % 2 == 0:
                nums[i] = even.pop(0)
            else:
                nums[i] = odd.pop(0)

        return nums