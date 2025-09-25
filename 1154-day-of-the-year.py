# https://leetcode.com/problems/day-of-the-year

import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        Y,m,d = date.split('-')
        date = datetime.datetime(int(Y), int(m), int(d))
        return date.timetuple().tm_yday