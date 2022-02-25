"""
253. Meeting Rooms II
Medium

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    def meeting_room_heap(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        rooms = []
        intervals.sort(key=lambda x: x[0])
        heappush(rooms, intervals[0][1])
        for i in intervals[1:]:
            if i[0] > rooms[0]:
                heappop(rooms)
            heappush(rooms, i[1])

    def meeting_rooms_start_end(self, intervals: List[List[int]]) -> int: 
        if not intervals: 
            return 0
        timestamp = []
        for s, e in intervals: 
            timestamp.extend([[s, 1], [e, -1]])
        timestamp.sort()
        rooms, ans = 0, 0
        for ts in timestamp:
            rooms += ts[1]
            ans = max(rooms, ans)
        return ans 

    def meeting_rooms_chrono_order(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        s_pt, e_pt = 0, 0
        num_rooms = 0
        while s_pt < len(start):
            if start[s_pt] < end[e_pt]:
                num_rooms += 1
            else:
                e_pt += 1
            s_pt += 1
        return num_rooms


"""
extension: finding a point where most intervals overlap
"""
class Extension:
    def ordering_solution(self, intervals: List[List[int]]) -> int:
        arrive = sorted([i[0] for i in intervals])
        departure = sorted([i[1] for i in intervals])
        a_pt, e_pt, ans = 0, 0, 0
        num_guest, max_guest = 1, 1
        while a_pt < len(arrive) and e_pt < len(departure):
            if arrive[a_pt] <= departure[e_pt]:
                num_guest += 1
                a_pt += 1
                if num_guest > max_guest:
                    max_guest, ans = num_guest, a_pt
            else:
                num_guest -= 1
                e_pt += 1
        return ans

    def one_arr_solution(self, intervals: List[List[int]]) -> int: 
        timestamp = []
        for a, d in intervals:
            # increment number of people at an arrival, decrement it at
            # departure 
            timestamp.extend([[a, 1], [d, -1]])
        timestamp.sort()
        n_people, ans = 0, [0,0]
        for ts in timestamp: 
            n_people += ts[1]
            ans = [ts[0], n_people] if n_people > ans[1] else ans
        return ans 



