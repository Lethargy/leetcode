# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts

class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'x' * n
        else:
            return 'x' * (n-1) + 'y'