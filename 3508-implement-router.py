# https://leetcode.com/problems/implement-router

from typing import List
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque([])
        self.map = defaultdict(list)
        self.seen = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source,destination,timestamp)
        if packet in self.seen:
            return False
        else:
            self.queue.append(packet)
            self.map[destination].append(packet)
            self.seen.add(packet)

            if len(self.queue) > self.memoryLimit:
                old = self.queue.popleft()
                self.map[old[1]].pop(0)
                self.seen.remove(old)
            return True
        
    def forwardPacket(self) -> List[int]:
        if self.queue:
            out = self.queue.popleft()
            self.map[out[1]].pop(0)
            self.seen.remove(out)
            return out
        else:
            return []
        
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        i = bisect_left(self.map[destination], startTime, key = lambda x: x[2])
        j = bisect_right(self.map[destination], endTime, key = lambda x: x[2])

        return j-i
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
        
