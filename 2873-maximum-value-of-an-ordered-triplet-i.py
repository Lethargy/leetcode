# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i

from typing import List

# dynamic programming

# Let v(k) denote the maximum value over nums[0],...,nums[k]
# At k, we have two choices:
#   1. Settle for nums[k]. Then, our value is maxDiff(k-1) * nums[k]
#   2. Pass up nums[k]. Then, our value is v(k-1)
# It follows that v(k) = max(maxDiff(k-1) * nums[k], v(k-1))
# with boundary condition v(2) = (nums[0]-nums[1]) * nums[2]
# Return v(n-1)

# maxDiff(j) is the maximum difference over nums[0],...,nums[j]
# Note that maxDiff(j) = max(runMax(j-1)-nums[j], maxDiff(j-1))
# with boundary condition maxDiff(1) = nums[0] - nums[1]

# runMax(i) is the running maximum over nums[0],...,nums[i]
# Note that runMax(i) = max(nums[i], runMax(i-1))
# with boundary condition runMax(0) = nums[0]

from functools import cache

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def value(k):
            if k == 2:
                return (nums[0]-nums[1])*nums[2]
            else:
                return max(maxDiff(k-1)*nums[k], value(k-1))
        
        @cache
        def maxDiff(j):
            if j == 1:
                return nums[0]-nums[1]
            else:
                return max(runMax(j-1)-nums[j], maxDiff(j-1))
        
        @cache
        def runMax(i):
            if i == 0:
                return nums[0]
            else:
                return max(nums[i], runMax(i-1))

        return value(n-1) if value(n-1) > 0 else 0

# Since the recursions have different boundary conditions,
# we'll need to modify them to tabularize
# Notice that value and maxDiff are defined as maximums, so take
# value[0] = 0 and maxDiff[0] = 0

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        value = [None] * n
        maxDiff = [None] * n
        runMax = [None] * n

        value[0] = 0
        maxDiff[0] = 0
        runMax[0] = nums[0]

        for i in range(1,n):
            value[i] = max(maxDiff[i-1]*nums[i], value[i-1])
            maxDiff[i] = max(runMax[i-1]-nums[i], maxDiff[i-1])
            runMax[i] = max(nums[i], runMax[i-1])
        
        return value[n-1]

# overwrite variables, and we get O(n) time, O(1) space
    
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        value = 0
        maxDiff = 0
        runMax = nums[0]

        for num in nums[1:]:
            value = max(maxDiff*num, value)
            maxDiff = max(runMax-num, maxDiff)
            runMax = max(num, runMax)
        
        return value
