# https://leetcode.com/problems/counting-bits

from typing import List

# i & (i-1) removes the least significant bit from i
# for example, if i = 10 = (1010)_2, then i-1 = 9 = (1001)_2
# i & (i-1) = (1000)_2
# to get the number of bits in i, we just add 1 to the number of bits in i & (i-1)

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(1,n+1):
            ans[i] = ans[i & (i-1)] + 1
        
        return ans