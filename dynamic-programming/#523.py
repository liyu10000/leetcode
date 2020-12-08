class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False
        for i in range(n-1):
            if nums[i] == nums[i+1] == 0:
                return True
        if k == 0:
            return False
        if k < 0:
            k = -k

        dp = [[0 for j in range(n)] for i in range(n)]
        for l in range(2, n+1):
            if l == 2:
                for i in range(n-1):
                    mod = (nums[i] + nums[i+1]) % k
                    if mod == 0:
                        return True
                    dp[i][i+1] = mod
            else:
                for i in range(n-l+1):
                    mod = (nums[i] + dp[i+1][i+l-1]) % k
                    if mod == 0:
                        return True
                    dp[i][i+l-1] = mod
        return False