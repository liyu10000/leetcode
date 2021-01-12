# brute force
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:    
        n = len(nums)
        if n <= k:
            return nums
        res = []
        cur = 0
        MAX = 10**9
        for i in range(k):
            sidx = cur
            sval = MAX
            for j in range(cur, n-k+i+1):
                if nums[j] < sval:
                    sidx = j
                    sval = nums[j]
            res.append(sval)
            cur = sidx + 1
        return res

# use stack
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s = []
        for i, num in enumerate(nums):
            min_len = max(0, k-len(nums)+i)
            while len(s) > min_len and s[-1] > num:
                s.pop()
            s.append(num)
        return s[:k]