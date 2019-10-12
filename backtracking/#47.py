class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        visited = set()
        res = []
        for i,n in enumerate(nums):
            if not n in visited:
                visited.add(n)
                res += [[n] + subres for subres in self.permuteUnique(nums[:i]+nums[i+1:])]
        return res