# https://leetcode.com/problems/course-schedule-ii

# kahn's algorithm

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        ans = []

        for a,b in prerequisites:
            graph[b].append(a)
            indeg[a] = indeg[a] + 1

        queue = [k for k in range(numCourses) if indeg[k] == 0]

        while queue:
            course = queue.pop(0)
            ans.append(course)

            for adj in graph[course]:
                indeg[adj] = indeg[adj] - 1
                
                if indeg[adj] == 0:
                    queue.append(adj)
        
        if len(ans) == numCourses:
            return ans
        else:
            return []
