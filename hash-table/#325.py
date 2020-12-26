class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = {}
        s = 0
        c = 0
        for i in range(n):
            s += nums[i]
            if s == k:
                c = i + 1
            elif s - k in d:
                c = max(c, i - d[s-k])
            if not s in d:
                d[s] = i
        return c