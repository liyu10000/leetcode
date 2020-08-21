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
        sets = [[]]
        for n in nums:
            sets += [[n] + s for s in sets]
        return sets

# solution from leetcode
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sets = []
        for i in range(2**n, 2**(n+1)):
            bmask = bin(i)[3:]
            sets.append([nums[j] for j in range(n) if bmask[j] == '1'])
        return sets