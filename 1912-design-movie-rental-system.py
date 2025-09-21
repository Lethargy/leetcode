# https://leetcode.com/problems/design-movie-rental-system

from typing import List
from collections import defaultdict
from sortedcontainers import SortedSet

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented = defaultdict(SortedSet)
        self.rented = SortedSet()
        self.price = dict()

        for shop,movie,price in entries:
            self.unrented[movie].add((price,shop))
            self.price[(movie,shop)] = price

    def search(self, movie: int) -> List[int]:
        return [shop for _,shop in self.unrented[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.price[(movie,shop)]
        self.rented.add((price,shop,movie))
        self.unrented[movie].remove((price,shop))
        
    def drop(self, shop: int, movie: int) -> None:
        price = self.price[(movie,shop)]
        self.rented.remove((price,shop,movie))
        self.unrented[movie].add((price,shop))
        
    def report(self) -> List[List[int]]:
        return [[shop,movie] for _,shop,movie in self.rented[:5]]
        
# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()