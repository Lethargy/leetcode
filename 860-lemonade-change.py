# https://leetcode.com/problems/lemonade-change

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives = fives + 1
            elif bill == 10 and fives >= 1:
                tens = tens + 1
                fives = fives - 1
            elif bill == 20 and tens >= 1 and fives >= 1:
                fives = fives - 1
                tens = tens - 1
            elif bill == 20 and fives >= 3:
                fives = fives - 3
            else:
                return False

        return True 