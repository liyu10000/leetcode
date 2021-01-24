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

# dp, get TLE
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i] means if it can reach n-1 from i
        dp = [0] * n # 0 for unknown, 1 for reachable, -1 for unreachable
        dp[n-1] = 1
        
        def helper(i):
            if dp[i] != 0:
                return True if dp[i] == 1 else False
            furthest = min(i + nums[i], n-1)
            for nexti in range(i+1, furthest+1):
                if helper(nexti):
                    dp[i] = 1
                    return True
            dp[i] = -1
            return False
        
        return helper(0)

# dp, get TLE
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i] means if it can reach i from 0
        dp = [0] * n # 1 for reachable, 0 for unreachable
        dp[0] = 1
        for i in range(n):
            if dp[i]:
                for j in range(i+1, min(i+nums[i]+1, n)):
                    dp[j] = 1
        return dp[n-1]

# improved dp
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i] means if it can reach i from 0
        dp = [0] * n # 1 for reachable, 0 for unreachable
        dp[0] = 1
        right = 0
        for i in range(n):
            if dp[i]:
                for j in range(right+1, min(i+nums[i]+1, n)):
                    dp[j] = 1
                    right = j
        return dp[n-1]

# greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        right = 0
        for i in range(n):
            if i <= right:
                right = max(right, i+nums[i])
        return right >= n-1