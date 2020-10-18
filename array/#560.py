# brute force, TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        sums = [0] * (length + 1)
        for i in range(1, length+1):
            sums[i] = sums[i-1] + nums[i-1]
        cnt = 0
        for i in range(length):
            for j in range(i+1, length+1):
                if sums[j] - sums[i] == k:
                    cnt += 1
        return cnt