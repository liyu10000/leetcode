# solution 1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def swap(i, res):
            if i == len(nums):
                res.append(nums[:])
            else:
                for j in range(i, len(nums)):
                    nums[i], nums[j] = nums[j], nums[i]
                    swap(i+1, res)
                    nums[i], nums[j] = nums[j], nums[i]
                    
        res = []
        swap(0, res)
        return res

# solution 2
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def add(entry, res):
            if len(entry) == len(nums):
                res.append(entry)
            else:
                for a in nums:
                    if not a in entry:
                        add(entry+[a], res)
                    
        res = []
        add([], res)
        return res

# back tracking
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