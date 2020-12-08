class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0] * n
        dp2 = [0] * n
        # count the increasing nums from 0 to i
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i] and dp1[i] < dp1[j] + 1:
                    dp1[i] = dp1[j] + 1
        # count the increasing nums from n-1 to i
        for i in range(n-2, -1, -1):
            for j in range(n-1, i, -1):
                if nums[j] < nums[i] and dp2[i] < dp2[j] + 1:
                    dp2[i] = dp2[j] + 1
        print(dp1)
        print(dp2)
        # get the maximum sum of counts
        m = 0
        for i in range(1,n-1): # skip first and last because they cannot be the peak
            m = max(m, dp1[i]+dp2[i])
        return n - m - 1