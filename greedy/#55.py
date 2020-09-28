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

# third try
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        flag = True
        lastTrue = n - 1
        for i in range(n-2, -1, -1):
            if (flag and nums[i] >= 1) or (not flag and nums[i] >= lastTrue-i):
                flag = True
                lastTrue = i
            else:
                flag = False
        return flag