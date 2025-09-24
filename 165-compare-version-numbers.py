# https://leetcode.com/problems/compare-version-numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split('.')
        b = version2.split('.')

        i = 0

        while i < len(a) and i < len(b):
            if int(a[i]) < int(b[i]):
                return -1
            elif int(a[i]) > int(b[i]):
                return 1
            else:
                i += 1

        while i < len(a):
            if int(a[i]) > 0:
                return 1
            else:
                i += 1

        while i < len(b):
            if int(b[i]) > 0:
                return -1
            else:
                i += 1

        return 0