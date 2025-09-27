# https://leetcode.com/problems/valid-triangle-number

from typing import List

# binary search
# O(n**2 log n) time, O(1) space

from bisect import bisect_right

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        for k in reversed(range(2,n)):
            for j in reversed(range(1,k)):
                i = bisect_right(nums, nums[k]-nums[j], hi = j)
                ans += j-i

        return ans
    
# two pointers

# O(n**2) time, O(1) space

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        for k in reversed(range(2,n)):
            i = 0
            j = k-1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1

        return ans