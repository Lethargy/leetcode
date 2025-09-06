# https://leetcode.com/problems/course-schedule/description

# kahn's algorithm

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        completed = 0

        for a,b in prerequisites:
            graph[b].append(a)
            indeg[a] = indeg[a] + 1

        queue = [n for n in range(numCourses) if indeg[n] == 0]

        while queue:
            course = queue.pop()
            completed = completed + 1

            for adj in graph[course]:
                indeg[adj] = indeg[adj] - 1

                if indeg[adj] == 0:
                    queue.append(adj)

        return completed == numCourses