"""
253. Meeting Rooms II (Medium, 30 fb tagged 0-6 months)
https://leetcode.com/problems/meeting-rooms-ii/

given an array of meeting time intervals intervals, intervals[i] = [start_i, end_i], return the minimum number of
conference rooms required.
"""
from typing import List
import heapq


class Solution:
    # Approach 1
    # use a heap to store the "earliest" freeing room time
    # compare each meeting with the earliest freeing time
    # 1. if start_i is larger -> can reuse room
    # 2. else -> need another room
    def min_rooms_heap(self, intervals: List[List[int]]) -> int:
        """
        time: O(NlogN) - sort O(NlogN) + iteration with heap operation O(NlogN)
        :param intervals: O(N) - heap
        :return:
        """
        intervals.sort()
        room_q, rooms = [], 0
        heapq.heapify(room_q)
        for s, e in intervals:
            if not room_q or s < room_q[0]:
                # no room or earliest freeing room frees after start time
                # need another room
                rooms += 1
            else:
                heapq.heappop(room_q)
            heapq.heappush(room_q, e)
        return rooms

    # Approach 2
    # separate start, end time array with separate pointers
    # if start pointer value > end pointer value -> a meeting starts after latest meeting ends
    # else -> need another room
    # examine every start time, we don't need to explore every end time
    def min_rooms_arrs(self, intervals: List[List[int]]) -> int:
        """
        time: O(NlogN) - O(NlogN) sorting for both start and end array + O(N) iterate through start times
        space: O(N) - O(2N) for start and end array
        :param intervals:
        :return:
        """
        start = sorted([s for s, e in intervals])
        end = sorted([e for s, e in intervals])
        s_idx, e_idx = 0, 0
        rooms = 0
        while s_idx < len(start):
            if start[s_idx] >= end[e_idx]:
                # meeting start after current end pointer -> we can reuse the meeting room
                # however, current room end time is not valid anymore, increment end pointer
                # to next meeting end time
                e_idx += 1
            else:
                # start[s_idx] < end[e_idx], we need another room to accommodate the new meeting
                # previous meeting has not ended, end pointer remains there for future meeting
                rooms += 1
            # explore next meeting start time
            s_idx += 1
        return rooms

    # Approach 3
    # initiate a timestamp array
    # append each meeting start and end time to timestamp array, with +1 for start and -1 for end
    # (ts, 1/-1) - this indicate needing a room when meeting start, and freeing a room when meeting ends
    # sort timestamp array
    # iterate through timestamp array and increment rooms, update max room count in the process

    def min_rooms_arr(self, intervals: List[List[int]]) -> int:
        """
        time: O(NlogN) - sorting timestamp array O(2Nlog2N), reduced to O(NlogN) + iterate through timestamp O(2N),
              reduced to O(N)
        space: O(N) - for timestamp array O(2N) reduced to O(N)
        :param intervals:
        :return:
        """
        ans, rooms = 0, 0
        timestamp = []
        for s, e in intervals:
            timestamp.append((s, 1))
            timestamp.append((e, -1))
        timestamp.sort()
        for ts, val in timestamp:
            rooms += val
            ans = max(rooms, ans)
        return ans
