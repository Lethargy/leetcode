# https://leetcode.com/problems/distribute-candies-to-people

from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        c = 1
        ans = [0] * num_people

        while candies > 0:
            ans[(c-1) % num_people] += min(c,candies)
            candies -= min(c,candies)
            c = c + 1

        return ans