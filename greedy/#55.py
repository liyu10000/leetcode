# first try: Time Limit Exceeded
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        for i in range(1, nums[0]+1):
            if self.canJump(nums[i:]):
                return True
        return False

# second try
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True

        n = len(nums)
        max_step = 0

        for i in range(n):
            if max_step < i:
                return False
            max_step = max(max_step, i + nums[i])

        return max_step >= n - 1