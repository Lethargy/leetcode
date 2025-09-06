# https://leetcode.com/problems/longest-increasing-subsequence

# pure recursive DP -- DO NOT implement

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def dp(i): # longest subsequence starting at i
            if i == n-1:
                return 1
            
            options = [j for j in range(i+1,n) if nums[j] > nums[i]]
            
            if len(options) > 0:
                return 1 + max(dp(j) for j in options)
            else:
                return 1

        return max(dp(i) for i in range(n))

class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n

        for i in reversed(range(n-1)):
            options = [j for j in range(i+1,n) if nums[j] > nums[i]]
            if len(options) > 0:
                dp[i] = 1 + max(dp[j] for j in options)
        
        return max(dp)