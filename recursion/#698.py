class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        ss = sum(nums)
        if ss % k != 0:
            return False
        
        target = ss // k
        visited = [False] * len(nums)
        return self.partition(nums, k, target, 0, 0, visited)
    
    def partition(self, nums, k, target, start, curSum, visited):
        if k == 1:
            return True
        if target == curSum:
            return self.partition(nums, k-1, target, 0, 0, visited)
        for i in range(start, len(nums)):
            if visited[i]:
                continue
            if nums[i] + curSum > target:
                continue
            visited[i] = True
            if self.partition(nums, k, target, i+1, nums[i]+curSum, visited):
                return True
            visited[i] = False
        return False