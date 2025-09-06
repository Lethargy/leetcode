# https://leetcode.com/problems/defuse-the-bomb

from typing import List

# sliding window

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        if k == 0:
            return ans
        
        a = 1 if k > 0 else k % n
        b = k if k > 0 else (-1) % n
            
        for i in range(a,b+1):
            ans[0] = ans[0] + code[i%n]
        
        for i in range(1,n):
            b = b + 1
            ans[i] = ans[i-1] + code[b%n] - code[a%n]
            a = a + 1
        
        return ans