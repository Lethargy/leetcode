# https://leetcode.com/problems/get-maximum-in-generated-array

from functools import cache

# dynamic progrmaming

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        @cache
        def nums(i):
            if i == 0:
                return 0
            elif i == 1:
                return 1
            elif i%2 == 0:
                return nums(i//2)
            else:
                return nums(i//2) + nums(1+i//2)
        
        @cache
        def M(i):
            if i == 0:
                return nums(0)
            else:
                return max(M(i-1), nums(i))

        return M(n)

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
            
        nums = [None] * (n+1)
        nums[0] = 0
        nums[1] = 1

        for i in range(2,n+1):
            if i % 2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[i//2+1]
        
        return max(nums)