# https://leetcode.com/problems/maximum-length-of-pair-chain

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()
        n = len(pairs)

        def v(i):
            if i == n-1:
                return 1
            
            options = [j for j in range(i+1,n) if pairs[j][0] > pairs[i][1]]
            
            if options:
                return 1 + max(v(j) for j in options)
            else:
                return 1

        return max(v(i) for i in range(n))
        
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()
        n = len(pairs)
        v = [1] * n

        for i in reversed(range(n-1)):
            options = [j for j in range(i+1,n) if pairs[j][0] > pairs[i][1]]

            if options:
                v[i] = 1 + max(v[j] for j in options)

        return max(v)