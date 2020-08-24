class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        while low <= high:
            while low+1 < len(nums) and nums[low] == nums[low+1]:
                low += 1
            while 0 < high and nums[high-1] == nums[high]:
                high -= 1
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
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
        return False