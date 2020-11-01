# Stack
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack, res = [], [-1] * n
        for i in range(n * 2):
            while stack and (nums[stack[-1]] < nums[i%n]):
                res[stack.pop()] = nums[i%n]
            stack.append(i%n)
        return res
        