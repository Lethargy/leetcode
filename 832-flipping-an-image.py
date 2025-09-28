# https://leetcode.com/problems/flipping-an-image

from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        m = len(image[0])

        for i in range(n):
            image[i] = list(reversed(image[i]))
            for j in range(m):
                image[i][j] = 1 - image[i][j]
        
        return image