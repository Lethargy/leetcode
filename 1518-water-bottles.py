# https://leetcode.com/problems/water-bottles

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        empty = numBottles

        while empty >= numExchange:
            empty -= numExchange
            drank += 1
            empty += 1
            
        return drank