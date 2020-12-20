# remember last index, got TLE
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        lastIndex = {}
        res = 0
        i = 0
        for j in range(n):
            i = max(i, lastIndex.get(nums[j],-1)+1)
            res = max(res, sum(nums[i:j+1]))
            lastIndex[nums[j]] = j
        return res

# similar, but with incremental sum
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        lastIndex = {}
        res = 0
        i = 0
        curSum = 0
        for j in range(n):
            newi = max(i, lastIndex.get(nums[j],-1)+1)
            for ii in range(i, newi):
                curSum -= nums[ii]
            curSum += nums[j]
            res = max(res, curSum)
            i = newi
            lastIndex[nums[j]] = j
        return res

# use indicator array instead of map, slightly faster
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        lastIndex = [-1] * int(1e4+1)
        res = 0
        i = 0
        curSum = 0
        for j in range(n):
            newi = max(i, lastIndex[nums[j]]+1)
            for ii in range(i, newi):
                curSum -= nums[ii]
            curSum += nums[j]
            res = max(res, curSum)
            i = newi
            lastIndex[nums[j]] = j
        return res

# use prefix sum
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        lastIndex = [-1] * int(1e4+1)
        preSum = [0] * (n+1)
        res = 0
        i = 0
        for j in range(n):
            preSum[j+1] = nums[j] + preSum[j]
            i = max(i, lastIndex[nums[j]]+1)
            res = max(res, preSum[j+1]-preSum[i])
            lastIndex[nums[j]] = j
        return res