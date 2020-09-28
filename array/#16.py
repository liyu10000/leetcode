class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sys.maxsize
        
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
                
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                elif s > target:
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                else:
                    return res
                
        return res


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        n = len(nums)
        for i in range(n-2):
            if diff == 0:
                return target
            left = i + 1
            right = n - 1
            while left < right:
                tmpsum = nums[i] + nums[left] + nums[right]
                if abs(target - tmpsum) < abs(diff):
                    diff = target - tmpsum
                if tmpsum > target:
                    right -= 1
                else:
                    left += 1
        return target - diff