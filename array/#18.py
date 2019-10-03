class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        res = []
        l = len(nums)
        for i in range(l-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, l-2):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                m, n = j+1, l-1
                while m < n:
                    s = nums[i] + nums[j] + nums[m] + nums[n]
                    if s < target:
                        m += 1
                    elif s > target:
                        n -= 1
                    else:
                        res.append([nums[i], nums[j], nums[m], nums[n]])
                        while m < n and nums[m] == nums[m+1]:
                            m += 1
                        while m < n and nums[n] == nums[n-1]:
                            n -= 1
                        m += 1
                        n -= 1

        return res