# https://leetcode.com/problems/minimum-number-of-people-to-teach

from collections import Counter
from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(language) for language in languages]
        teach = set()
        for u,v in friendships:
            if not languages[u-1] & languages[v-1]:
                teach.add(u)
                teach.add(v)
        
        langCount = Counter()
        for u in teach:
            for language in languages[u-1]:
                langCount[language] += 1
        
        return len(teach) - max(langCount.values(), default = 0)