# brute force, got TLE
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        dp = [2**32 for _ in range(n)]
        for i in range(n):
            for j in range(i+1, min(i+k+1, n)):
                dp[i] = min(dp[i], abs(nums[j] - nums[i]))
            if dp[i] <= t:
                return True
        # print(dp)
        return False

