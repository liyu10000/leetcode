class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in d:
                return [d[diff], i]
            else:
                d[n] = i
        return [-1, -1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffmap = {}
        for i,n in enumerate(nums):
            if n in diffmap:
                return [diffmap[n], i]
            diffmap[target - n] = i
        return []