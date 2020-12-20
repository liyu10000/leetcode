from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        def clean(i):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
        
        n = len(nums)
        dq = deque()
        res = []
        for i in range(n):
            clean(i)
            dq.append(i)
            if i >= k-1:
                res.append(nums[dq[0]])
            # print(i, dq)
        return res