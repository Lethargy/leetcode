# https://leetcode.com/problems/count-largest-group

from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = Counter()

        for k in range(1,n+1):
            s = sum(int(d) for d in str(k))
            count[s] += 1
        
        return sum(v == max(count.values()) for v in count.values())