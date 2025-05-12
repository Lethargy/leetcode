# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference

class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        n = len(arr)
        def v(i):
            if i == n-1:
                return 1
            
            k = min([j for j in range(i+1,n) if arr[j] == arr[i] + difference] + [float('inf')])

            if k < float('inf'):
                return 1 + v(k)
            else:
                return 1

        return max(v(i) for i in range(n))
    
class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        n = len(arr)
        v = [1] * n
        idx = {arr[n-1]: n-1} # index lookup dictionary; idx[arr[j]] = j

        for i in reversed(range(n-1)):
            a = arr[i] + difference

            if a in idx:
                v[i] = 1 + v[idx[a]]

            idx[arr[i]] = i

        return max(v)