# https://leetcode.com/problems/permutations/description/

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        stack = [([],nums)]

        while stack:
            path, rem = stack.pop()

            if not rem:
                ans.append(path)
                continue

            for r in rem:
                rem2 = rem + []
                rem2.remove(r)
                stack.append((path + [r], rem2))

        return ans