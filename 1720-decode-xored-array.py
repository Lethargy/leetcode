# https://leetcode.com/problems/decode-xored-array

from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        res = [first] + [None] * n

        for i,num in enumerate(encoded):
            res[i+1] = res[i] ^ encoded[i]

        return res