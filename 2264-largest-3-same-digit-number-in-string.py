# https://leetcode.com/problems/largest-3-same-digit-number-in-string

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        prev = num[0]
        streak = 1
        ans = ''

        for ch in num[1:]:
            if prev == ch:
                streak += 1
            else:
                streak = 1
            prev = ch

            if streak == 3:
                if not ans:
                    ans = ch
                if ans and ch > ans:
                    ans = ch
        return 3 * ans

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        M = -float('inf')

        for i in range(2,n):
            if num[i] == num[i-1] == num[i-2]:
                M = max(M, int(num[i]))
        
        if M > -float('inf'):
            return 3 * str(M)
        else:
            return ''






            


            
