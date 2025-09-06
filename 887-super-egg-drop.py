# https://leetcode.com/problems/super-egg-drop

from functools import cache

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        @cache
        def h(k,d):
            if k == 1:
                return d
            if d == 1:
                return 1

            return 1 + h(k-1,d-1) + h(k,d-1)

        ans = 1
        while h(k,ans) < n:
            ans = ans + 1

        return ans