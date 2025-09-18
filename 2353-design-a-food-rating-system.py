# https://leetcode.com/problems/design-a-food-rating-system

from typing import List
from collections import defaultdict

# using priority queues

from heapq import heappush, heappop

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.catalog = defaultdict(list)
        self.foodScore = dict()
        self.foodCuisine = dict()

        for food,cuisine,rating in zip(foods,cuisines,ratings):
            score = -(26 * rating + ord('z') - ord(food[0]))
            heappush(self.catalog[cuisine], (score,food))
            self.foodScore[food] = score
            self.foodCuisine[food] = cuisine

    def changeRating(self, food: str, newRating: int) -> None:
        newScore = -(26 * newRating + ord('z') - ord(food[0]))
        cuisine = self.foodCuisine[food]
        heappush(self.catalog[cuisine], (newScore,food))
        self.foodScore[food] = newScore
        
        bestScore, bestFood = self.catalog[cuisine][0]
        while bestScore != self.foodScore[bestFood]:
            heappop(self.catalog[cuisine])
            bestScore, bestFood = self.catalog[cuisine][0]

    def highestRated(self, cuisine: str) -> str:
        return self.catalog[cuisine][0][1]


# using sorted sets

from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.catalog = defaultdict(lambda: SortedSet(key = lambda x: (-x[0],x[1])))
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