# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i

# sliding window

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        ones = zeroes = 0
        i = 0

        for j in range(n):
            if s[j] == '1':
                ones += 1
            else:
                zeroes += 1
            
            while ones > k and zeroes > k:
                if s[i] == '1':
                    ones -= 1
                else:
                    zeroes -= 1
                i += 1
            
            ans += j-i+1

        return ans