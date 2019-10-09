class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                pl = mid
                while pl >= 0 and nums[pl] == target:
                    pl -= 1
                ph = mid
                while ph < len(nums) and nums[ph] == target:
                    ph += 1
                return [pl+1, ph-1]
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [-1, -1]