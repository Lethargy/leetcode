# https://leetcode.com/problems/check-if-n-and-its-double-exist

from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        need = set()
        for a in arr:
            if a in need:
                return True
            
            need.add(2*a)

            if a % 2 == 0:
                need.add(a // 2)

        return False
    
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for a in arr:
            if 2*a in seen or (a%2==0 and a//2 in seen):
                return True
            seen.add(a)

        return False