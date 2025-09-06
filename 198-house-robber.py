# https://leetcode.com/problems/house-robber

# pure recursive DP -- DO NOT implement

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def v(i):                
            if i == n-1:
                return nums[n-1]
            
            if i == n-2:
                return max(v(i+1), nums[i])

            return max(v(i+1), nums[i] + v(i+2))

        return v(0)
    
# tabularized; O(n) complexity, O(1) memory
    
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        v = [None] * n
        v[n-1] = nums[n-1]
        v[n-2] = max(v[n-1], nums[n-2])

        for i in reversed(range(n-2)):
            v[i] = max(v[i+1], nums[i] + v[i+2])

        return v[0]
    
# O(n) complexity, O(1) memory
    
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        v2 = 0
        v1 = nums[n-1]

        for i in reversed(range(n-1)):
            v0 = max(v1, nums[i] + v2)
            v2,v1 = v1,v0

        return v1