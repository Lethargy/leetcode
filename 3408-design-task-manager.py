# https://leetcode.com/problems/design-task-manager

from typing import List

# using balanced search tree / sorted set

from sortedcontainers import SortedSet
    
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = SortedSet(key = lambda x: (-x[0],-x[1]))
        self.user = dict()
        self.priority = dict()

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        t = (priority,taskId,userId)
        self.tasks.add(t)
        self.user[taskId] = userId
        self.priority[taskId] = priority

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.user[taskId]
        oldPriority = self.priority[taskId]
        self.tasks.remove((oldPriority,taskId,userId))
        self.tasks.add((newPriority,taskId, userId))
        self.priority[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        userId = self.user[taskId]
        priority = self.priority[taskId]
        self.tasks.remove((priority,taskId,userId))
        del self.user[taskId]
        del self.priority[taskId]

    def execTop(self) -> int:
        if self.tasks:
            return self.tasks.pop(0)[2]
        else:
            return -1

# using heap

from heapq import heappush, heappop, heapify

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = []
        self.user = dict()
        self.priority = dict()

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        t = (-priority,-taskId,userId)
        heappush(self.tasks, t)
        self.user[-taskId] = userId
        self.priority[-taskId] = -priority

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.user[-taskId]
        t = (-newPriority,-taskId, userId)
        self.priority[-taskId] = -newPriority
        heappush(self.tasks, t)

    def rmv(self, taskId: int) -> None:
        del self.user[-taskId]
        del self.priority[-taskId]

    def execTop(self) -> int:
        while self.tasks:
            topPriority, topTask, topUser = heappop(self.tasks)

            if topTask not in self.priority:
                continue
            
            if self.priority[topTask] != topPriority:
                continue

            if self.user[topTask] != topUser:
                continue

            del self.user[topTask]
            del self.priority[topTask]
            return topUser
        
        return -1