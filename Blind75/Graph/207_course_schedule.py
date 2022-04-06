"""
207. Course Schedule (Medium, 12 fb tagged 0~6 mth)
https://leetcode.com/problems/course-schedule/

total of numCourses courses you have to take (0 to numCourses - 1).
prerequisite array where prerequisite[i] = [ai, bi] indicates bi must be taken before ai

return true if you can finish all courses, else return false
"""
from typing import List
from collections import defaultdict, deque

# if we find a cycle within the graph, then it's not feasible

class Solution:
    def can_finish_topological_sort(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        use topological sort
        time: O(E + V)
        space: O(E + V)
        :param numCourses:
        :param prerequisites:
        :return:
        """
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for post, prev in prerequisites:
            graph[prev].append(post)
            in_degree[post] += 1

        queue = deque([i for i, c in enumerate(in_degree) if c == 0])
        taken = 0
        while queue:
            head = queue.popleft()
            taken += 1
            for nei in graph[head]:
                in_degree[nei] -= 1
                if in_degree == 0:
                    queue.append(nei)

        return taken == numCourses

    def can_finish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        DFS approach
        time: O(V + E)
        space: O(V + E)
        :param numCourses:
        :param prerequisites:
        :return:
        """
        graph = defaultdict(list)
        for post, prev in prerequisites:
            graph[prev].append(post)

        visited, stream = set(), set()
        has_cycle = False

        def dfs(i):
            if i in stream:
                nonlocal has_cycle
                has_cycle = True
                return
            stream.add(i)
            for ni in graph[i]:
                if ni not in visited:
                    dfs(ni)
            stream.remove(i)
            visited.add(i)

        for course in range(numCourses):
            if course not in visited:
                dfs(course)
                if has_cycle:
                    return False
        return True