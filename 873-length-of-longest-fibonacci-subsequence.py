from typing import List
from functools import cache

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        
        @cache
        def A(i):
            if i == n-1:
                return 1
            
            return max(A(i+1), 1 + B(i+1,arr[i]))
        
        @cache
        def B(i,a0):
            if i == n-1:
                return 1
            
            return max(B(i+1,a0), 1 + C(i+1,a0,arr[i]))
        
        @cache
        def C(i,a0,a1):
            if i == n:
                return 0

            if arr[i] == a0 + a1:
                return 1 + C(i+1,a1,arr[i])
            else:
                return C(i+1,a0,a1)

        ans = A(0)
        if ans < 3:
            return 0
        else:
            return ans
        
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)

        @cache
        def A(i):
            if i == n-1:
                return 1
            
            return max(A(i+1), 1 + B(i+1,arr[i]))
        
        @cache
        def B(i,a0):
            if i == n-1:
                return 1
            
            return max(B(i+1,a0), 1 + C(a0,arr[i]))

        S = set(arr)
        def C(a0,a1):
            ans = 0
            while a0 + a1 in S:
                ans = ans + 1
                a0, a1 = a1, a0 + a1

            return ans

        ans = A(0)
        if ans < 3:
            return 0
        else:
            return ans
        
    
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        ind = {arr[i]:i for i in range(n)}

        @cache
        def v(i,j):
            ak = arr[i] + arr[j] 
            if ak not in ind:
                return 2
            else:
                return 1 + v(j,ind[ak])

        ans = max(v(i,j) for i in range(n) for j in range(i+1,n))
        return ans if ans >= 3 else 0
    
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        ind = {arr[i]:i for i in range(n)}
        v = [[2] * (k+1) for k in range(n)]
        ans = 0

        for i in reversed(range(n)):
            for j in reversed(range(i+1,n)):
                ak = arr[i] + arr[j]
                if ak in ind:
                    v[j][i] = 1 + v[ind[ak]][j]
                ans = max(ans, v[j][i])
        
        return ans if ans >= 3 else 0