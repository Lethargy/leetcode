# https://leetcode.com/problems/shortest-completing-word

from typing import List
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        count = Counter()

        for ch in licensePlate:
            if ch.isalpha():
                count[ch.lower()] += 1
        
        words.sort(key = len)
        for word in words:
            if count <= Counter(word):
                return word