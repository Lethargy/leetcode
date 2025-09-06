# https://leetcode.com/problems/max-pair-sum-in-an-array

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def maxDigit(num):
            ans = 0
            while num > 0:
                num, rem = num // 10, num % 10
                ans = max(ans, rem)
            return ans
        
        ans = -1
        maxNum = [0] * 10
        for num in nums:
            d = maxDigit(num)
            if maxNum[d] > 0:
                ans = max(ans, maxNum[d] + num)
            maxNum[d] = max(maxNum[d], num)
        
        return ans
