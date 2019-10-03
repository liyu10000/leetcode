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
                        