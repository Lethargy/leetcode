# https://leetcode.com/problems/water-bottles-ii

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            emptyBottles -= numExchange
            drank += 1
            emptyBottles += 1
            numExchange += 1
        
        return drank

