# https://leetcode.com/problems/divisor-game

# If n = 1, Alice loses.
# If n = 2, Alice takes x = 1, and Bob loses.
# If n = 3, Alice must take x = 1. Bob inherits n = 2 and wins.
# If n = 4, Alice can
#   1. take x = 2. Bob inherits n = 2 and wins.
#   2. take x = 1. Bob inherits n = 3 and loses. In this case, Alice wins.

# The pattern is that if n is even, Alice wins.

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0