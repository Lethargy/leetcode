# https://leetcode.com/problems/find-center-of-star-graph

from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()