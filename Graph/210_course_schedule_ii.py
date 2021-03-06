"""
210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course
bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers,
return any of them. If it is impossible to finish all courses, return an empty array.
"""
import collections

"""
Idea
Input: List[List[int]]
Output: List[int]

What it should do
rank the order of prerequisite classes
Question: 
Could a class have multiple prerequisites? 
Would a cycle (a class's prereq had already been visited) indicate infeasibility? 
Or if there aren't nCourses classes in the input, exceeds nCourses? 
If no prereq, then can return anything? 

can we consider the input as a directed graph
vertex: a course
directed edge: prereq relationship, from -> to, class -> prereq? 
assume a connected graph for now
"""
from typing import List
from collections import defaultdict


class Solution:
    def topological_sorting(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        method: topological sorting
        time: O(E) to traverse through prerequisites, at most O(V) to traverse through the queue -> O(V+E)
        space: O(E) at most to store the graph, O(V) to store the queue -> O(V+E)
        :param numCourses:
        :param prerequisites:
        :return:
        """
        graph = defaultdict(list)
        in_degree = {}

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] = in_degree.get(dest, 0) + 1

        queue = collections.deque([i for i in range(numCourses) if i not in in_degree])
        ans = []

        while queue:
            v = queue.popleft()
            ans.append(v)
            for nei in graph[v]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        # if there's still vertex with non-zero in-degree (negative to be specific), we found a cycle
        return ans if len(ans) == numCourses else []


    def schedule(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        relationship = defaultdict(list)
        for c, p in prerequisites:
            relationship[c].append(p)
        ans, taking, stack = [], set(), set()
        has_cycle = False

        def find_prereq(course, visited, stream):
            nonlocal has_cycle
            if course in stream:
                has_cycle = True
                return
            visited.add(course)
            stream.add(course)
            if course in relationship:
                for prereq in relationship[course]:
                    if prereq not in visited:
                        find_prereq(prereq, visited, stream)
            ans.append(course)
            stream.remove(course)

        i = 0
        while i < numCourses:
            if not has_cycle:
                find_prereq(i, taking, stack)
                i += 1
            else:
                return []
        return ans

    def alternative(self, numCourses: int, prerequisite: List[List[int]]) -> List[int]:
        # state: 0 - not visited, 1 - visited but not done traverse, 2 - visited and traversed
        state = {i: 0 for i in range(numCourses)}
        relationship = defaultdict(list)
        for c, p in prerequisite:
            relationship[c].append(p)
        ans = []
        cycle = False

        def dfs(node):
            nonlocal cycle
            if cycle:
                return
            state[node] = 1
            if node in relationship:
                for neighbor in relationship[node]:
                    if state[neighbor] == 0:
                        dfs(neighbor)
                    elif state[neighbor] == 1:
                        cycle = True
            state[node] = 2
            ans.append(node)

        for v in range(numCourses):
            if state[v] == 0:
                dfs(v)
        return ans if not cycle else []



