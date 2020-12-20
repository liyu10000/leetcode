# naive dp, get TLE
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-1e4] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + max(dp[max(i-k,0):i])
        # print(dp)
        return dp[n-1]

# use deque to get sliding window max
from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        def clean(i):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and dp[i] > dp[dq[-1]]:
                dq.pop()
        
        n = len(nums)
        dp = [0] * n
        dq = deque()
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            else:
                clean(i-1)
                dq.append(i-1)
                dp[i] = nums[i] + dp[dq[0]]
            # print(i, dp, dq)
        return dp[n-1]