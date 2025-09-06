# https://leetcode.com/problems/day-of-the-week

from datetime import date

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = {0: 'Monday', 1: 'Tuesday', 2:'Wednesday', 3:'Thursday',
        4:'Friday', 5:'Saturday', 6:'Sunday'}

        return week[date(year, month, day).weekday()]