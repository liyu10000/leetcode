class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m, c = float('inf'), 0
        for n in nums:
            m = min(m, n)
            c += n
        return c - m * len(nums)

# more concise
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)