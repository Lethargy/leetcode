# https://leetcode.com/problems/design-spreadsheet

from collections import defaultdict

class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.grid[cell] = value

    def resetCell(self, cell: str) -> None:
        self.grid[cell] = 0
        
    def getValue(self, formula: str) -> int:
        X,Y = formula[1:].split('+')

        val1 = self.grid[X] if X[0].isalpha() else int(X)
        val2 = self.grid[Y] if Y[0].isalpha() else int(Y)

        return val1 + val2

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)