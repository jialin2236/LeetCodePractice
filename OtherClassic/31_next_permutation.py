class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while nums[i] <= nums[i-1] and i >= 1:
            i -= 1
        j = i
        while j < n and i > 0 and nums[j] > nums[i-1]:
            j += 1
        nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
        left, right = i, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    l = [3,2,1]
    solve = Solution()
    print(l)
    solve.nextPermutation(l)
    print(l)