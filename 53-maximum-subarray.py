# https://leetcode.com/problems/maximum-subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        v = [None] * n
        v[n-1] = nums[n-1]

        for i in reversed(range(n-1)):
            v[i] = nums[i] + max(v[i+1], 0)

        return max(v)
        
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        v = nums[n-1]
        ans = nums[n-1]

        for i in reversed(range(n-1)):
            v = nums[i] + max(v, 0)
            ans = max(ans, v)

        return ans