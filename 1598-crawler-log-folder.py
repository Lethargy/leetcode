# https://leetcode.com/problems/crawler-log-folder

from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0

        for op in logs:
            if op == '../':
                ans = max(0, ans - 1)
            elif op == './':
                continue
            else:
                ans += 1
        
        return ans