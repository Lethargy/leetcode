# https://leetcode.com/problems/minimum-index-sum-of-two-lists

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx = dict()
        for i,word in enumerate(list1):
            idx[word] = [i]
        for i,word in enumerate(list2):
            if word in idx:
                idx[word].append(i)
        
        ans = []
        M = float('inf')

        for word,indices in idx.items():
            if len(indices) == 1:
                continue
            
            if indices[0] + indices[1] < M:
                ans = [word]
                M = indices[0] + indices[1]
            elif indices[0] + indices[1] == M:
                ans.append(word)
        
        return ans

# slightly more efficient

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx = dict()
        for i,word in enumerate(list1):
            idx[word] = i

        ans = []
        M = float('inf')
        for j,word in enumerate(list2):
            if word not in idx:
                continue
            elif idx[word] + j < M:
                ans = [word]
                M = idx[word] + j
            elif idx[word] + j == M:
                ans.append(word)
        
        return ans

        