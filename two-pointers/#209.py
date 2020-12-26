# O(n^2), get TLE
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0] * (n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]
        if preSum[-1] < s:
            return 0
        # print(preSum)
        l = n
        for i in range(n):
            for j in range(i, min(n,i+l)):
                if preSum[j+1] - preSum[i] >= s:
                    l = min(l, j-i+1)
                    break
            if l == 1:
                return 1
            # print(i, j, l)
        return l

# two pointers
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        t = 0
        i = 0
        c = 2*n
        for j in range(n):
            t += nums[j]
            while i <= j and t >= s:
                c = min(c, j-i+1)
                t -= nums[i]
                i += 1
            # print(i, j, t, c)
            if c == 1:
                return 1
        return c if c < 2*n else 0