# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value

from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        count = Counter(num)

        for i,d in enumerate(num):
            if count[str(i)] != int(d):
                return False

        return True