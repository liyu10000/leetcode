class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2 # need to use l + (r - l) // 2 in case of overflow
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m
        return l