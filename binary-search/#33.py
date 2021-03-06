class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]: # on increasing
                    high = mid - 1
                else: # pivot in between
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]: # on increasing
                    low = mid + 1
                else: # pivot in between
                    high = mid - 1
        return -1