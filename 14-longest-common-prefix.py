# https://leetcode.com/problems/longest-common-prefix

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        while not all(s.startswith(prefix) for s in strs):
            prefix = prefix[:-1]

        return prefix
