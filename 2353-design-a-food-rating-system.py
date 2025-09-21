# https://leetcode.com/problems/design-a-food-rating-system

from typing import List
from collections import defaultdict

# using SortedList

from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.catalog = defaultdict(lambda: SortedList(key = lambda x: (-x[0],x[1])))
        self.foodRating = dict()
        self.foodCuisine = dict()

        for food,cuisine,rating in zip(foods,cuisines,ratings):
            self.catalog[cuisine].add((rating,food))
            self.foodRating[food] = rating
            self.foodCuisine[food] = cuisine

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = self.foodRating[food]
        cuisine = self.foodCuisine[food]
        self.catalog[cuisine].remove((oldRating,food))
        self.catalog[cuisine].add((newRating,food))
        self.foodRating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.catalog[cuisine][0][1]

# using heap

from heapq import heappush, heappop

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.catalog = defaultdict(list)
        self.foodRating = dict()
        self.foodCuisine = dict()

        for food,cuisine,rating in zip(foods,cuisines,ratings):
            heappush(self.catalog[cuisine], (-rating,food))
            self.foodRating[food] = -rating
            self.foodCuisine[food] = cuisine

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodCuisine[food]
        heappush(self.catalog[cuisine], (-newRating,food))
        self.foodRating[food] = -newRating
        
        bestRating, bestFood = self.catalog[cuisine][0]
        while bestRating != self.foodRating[bestFood]:
            heappop(self.catalog[cuisine])
            bestRating, bestFood = self.catalog[cuisine][0]

    def highestRated(self, cuisine: str) -> str:
        return self.catalog[cuisine][0][1]


