# https://leetcode.com/problems/number-of-different-integers-in-a-string

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = word + 'a'
        nums = set()
        num = ''

        for ch in word:
            if ch.isnumeric():
                num = num + ch
            if ch.isalpha() and len(num) > 0:
                nums.add(int(num))
                num = ''
        
        return len(nums)
