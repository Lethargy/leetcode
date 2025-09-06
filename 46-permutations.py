# https://leetcode.com/problems/permutations/description/

from typing import List

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

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        ans = []

        def dfs(path):
            if len(path) == n:
                ans.append(path.copy())

            for i,k in enumerate(nums):
                if used[i]:
                    continue

                path.append(k)
                used[i] = True
                dfs(path)
                path.pop()
                used[i] = False

        dfs([])
        return ans