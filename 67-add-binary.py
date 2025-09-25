# https://leetcode.com/problems/add-binary

# two pointers

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        c = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 and j >= 0:
            ans.append((int(a[i]) + int(b[j]) + c) % 2)
            c = (int(a[i]) + int(b[j]) + c) // 2
            i -= 1
            j -= 1

        while j >= 0:
            ans.append((int(b[j]) + c) % 2)
            c = (int(b[j]) + c) // 2
            j -= 1

        while i >= 0:
            ans.append((int(a[i]) + c) % 2)
            c = (int(a[i]) + c) // 2
            i -= 1

        if c: ans.append(c)

        return ''.join(str(a) for a in reversed(ans))