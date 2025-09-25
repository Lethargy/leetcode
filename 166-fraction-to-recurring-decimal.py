# https://leetcode.com/problems/fraction-to-recurring-decimal

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans = ''

        if numerator < 0 and denominator > 0:
            ans += '-'
            numerator = -numerator
        elif numerator > 0 and denominator < 0:
            ans += '-'
            denominator = -denominator
        elif numerator < 0 and denominator < 0:
            numerator = -numerator
            denominator = -denominator

        ans += str(numerator // denominator)
        numerator = 10 * (numerator % denominator)

        if numerator == 0:
            return ans

        ans += '.'
        seen = dict()
        d = []
        i = 0 # where to loop back

        while numerator > 0 and numerator not in seen:
            d.append(str(numerator // denominator))
            seen[numerator] = i
            i += 1
            numerator = 10 * (numerator % denominator)
        
        if numerator == 0:
            return ans + ''.join(d)
        else:
            i = seen[numerator]
            return ans + ''.join(d[:i]) + '(' + ''.join(d[i:]) + ')'