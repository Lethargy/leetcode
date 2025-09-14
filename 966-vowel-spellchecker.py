# https://leetcode.com/problems/vowel-spellchecker

from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def caseHash(s):
            return s.lower()
        
        def vowelHash(s):
            return s.lower().replace('e', 'a').replace('i', 'a').replace('o', 'a').replace('u', 'a')
        
        exact = set(wordlist)
        case = dict()
        vowl = dict()
        
        for w in wordlist:

            c = caseHash(w)
            if c not in case:
                case[c] = w

            v = vowelHash(w)
            if v not in vowl:
                vowl[v] = w
        
        def correct(w):
            if w in exact:
                return w

            c = caseHash(w)
            if c in case:
                return case[c]

            v = vowelHash(w)
            if v in vowl:
                return vowl[v]
                
            return ''
                    
        return [correct(q) for q in queries]