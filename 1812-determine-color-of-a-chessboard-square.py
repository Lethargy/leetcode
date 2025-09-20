# https://leetcode.com/problems/determine-color-of-a-chessboard-square

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col,row = coordinates
        return ord(col) % 2 != ord(row) % 2