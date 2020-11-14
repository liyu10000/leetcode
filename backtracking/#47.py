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

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cur):
            if len(cur) == n:
                res.append(cur)
                return
            for i in d.keys():
                if d[i] > 0:
                    d[i] -= 1
                    backtrack(cur+[i])
                    d[i] += 1
        nums.sort()
        # print(nums)
        n = len(nums)
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        # print(d)
        res = []
        backtrack([])
        return res