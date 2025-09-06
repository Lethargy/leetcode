# https://leetcode.com/problems/kth-missing-positive-number

from typing import List

# naive O(n)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        num = 1
        i = 0
        count = 0

        while count < k:
            if i < n and num == arr[i]:
                i += 1
            else:
                count += 1
            num += 1
        
        return num-1

# binary search O(log n)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def missing(i):
            return arr[i]-(i+1)

        i = 0
        j = len(arr) - 1

        if missing(0) >= k:
            return k
        
        if missing(j) < k:
            return arr[j] + k - missing(j)

        while j-i > 1:
            m = (i+j)//2
            if missing(m) < k <= missing(m+1):
                return arr[m] + k - missing(m)
            elif missing(m) >= k:
                j = m
            elif k > missing(m+1):
                i = m
        
        return arr[i] + k - missing(i)


