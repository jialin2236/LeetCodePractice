class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def pivot_search(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def bin_search(left, right):
            if left <= right:
                mid = (left + right)//2
                if target == nums[mid]:
                    return mid
                if target < nums[mid]:
                    return bin_search(left, mid-1)
                else:
                    return bin_search(mid+1, right)
            else:
                return -1

        k = len(nums) - 1
        if k == 0:
            return 0 if nums[0] == target else -1
        p = pivot_search(0, k)
        if p == 0:
            return bin_search(0, k)
        else:
            if target == nums[p]:
                return p
            if target < nums[0]:
                return bin_search(p+1, k)
            else:
                return bin_search(0, p-1)

    def searchm(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            if nums[left] < nums[mid]: # first half is non-rotated
                if nums[left] <= target < nums[mid]: # if target is in first half
                    right = mid - 1
                else: # target is not in first half
                    left = mid + 1
            else: # second half is non-rotated
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else: # target not in second half
                    right = mid - 1
        return -1




if __name__ == '__main__':
    s = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(s.search(nums,target))
