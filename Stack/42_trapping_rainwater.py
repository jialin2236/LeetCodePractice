"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""

"""
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        ans, size = 0, len(height)
        left_max, right_max = [], []
        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = height[i] if height[i] > left_max[i-1] else left_max[i-1]
        right_max[size-1] = height[size-1]
        for i in range(size-2,-1,-1):
            right_max[i] = height[i] if height[i] > right_max[i+1] else right_max[i+1]
        for i in range(1, size):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans

    def trap1(self, height):
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans

    def trapstack(self, height):
        i = 0
        ans = 0
        st = []
        while i < len(height):
            while st and height[i] > height[st[-1]]:
                top = st.pop()
                if not st:
                    break
                distance = i - st[-1] - 1
                bounded_height = min(height[i], height[-1]) - height[top]
                ans += distance * bounded_height
            i += 1
            st.append(i)
