# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def e(i):
            if i == n-1:
                return 1
            
            return 1 + max((e(k) for k in range(i+1,n) if (nums[i] + nums[k]) % 2 == 0), default = 0)
            
        @cache
        def o(i):
            if i == n-1:
                return 1

            return 1 + max((o(k) for k in range(i+1,n) if (nums[i] + nums[k]) % 2 == 1), default = 0)

        return max(max(o(k),e(k)) for k in range(n))

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        o = [1] * n
        e = [1] * n

        if nums[-1] % 2 == 0:
            Le = n-1 # last even index
            Lo = None # last odd index
        else:
            Le = None
            Lo = n-1

        for i in reversed(range(n-1)):
            if nums[i] % 2 == 0:
                e[i] = 1 + e[Le] if Le is not None else 1
                o[i] = 1 + o[Lo] if Lo is not None else 1
                Le = i
            else:
                e[i] = 1 + e[Lo] if Lo is not None else 1
                o[i] = 1 + o[Le] if Le is not None else 1
                Lo = i

        return max(max(e), max(o))