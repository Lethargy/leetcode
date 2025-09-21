# https://leetcode.com/problems/find-the-encrypted-string

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        ans = ''

        for i in range(n):
            ans += s[(i+k)%n]

        return ans