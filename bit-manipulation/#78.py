# first try
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def add(i, entry):
            if i == len(nums):
                res.append(entry)
            else:
                add(i+1, entry)
                add(i+1, entry+[nums[i]])
        
        res = []
        add(0, [])
        return res

# second try
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
        return res