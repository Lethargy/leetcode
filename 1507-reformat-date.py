# https://leetcode.com/problems/reformat-date

class Solution:
    def reformatDate(self, date: str) -> str:
        monthMap = {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        d,m,Y = date.split()

        if len(d) == 3:
            d = '0' + d[:-2]
        else:
            d = d[:-2]
        
        return f'{Y}-{monthMap[m]}-{d}'