# https://leetcode.com/problems/vowels-game-in-a-string

# Let n be the number of vowels in s.
# If n is 0, Alice loses.
# If n is odd, Alice picks the whole string and wins.
# If n is even, Alice picks any substring containing n-1 vowels.
# In this case, Bob is left with a string with 1 vowel.
# If he chooses a 0-vowel substring, he loses on the next turn.
# If he cannot chose a 0-vowel substring, he loses on that turn.

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return bool(set('aeiou') & set(s))

# faster

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in s for c in 'aeiou')