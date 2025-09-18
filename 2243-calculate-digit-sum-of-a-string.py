# https://leetcode.com/problems/calculate-digit-sum-of-a-string

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            t = ''
            for i in range(0,len(s),k):
                t += str(sum(int(c) for c in s[i:i+k]))
            s = t
        
        return s
                
        
                
        