from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        i, j = 0, 0
        minq, maxq = deque(), deque()
        res = 0
        while j < n:
            # ensure decreasing order
            while minq and nums[minq[-1]] < nums[j]:
                minq.pop()
            minq.append(j)
            # ensure increasing order
            while maxq and nums[maxq[-1]] > nums[j]:
                maxq.pop()
            maxq.append(j)
            # ensure maxValue - minValue <= limit
            while nums[minq[0]] - nums[maxq[0]] > limit:
                i += 1
                if i > minq[0]:
                    minq.popleft()
                if i > maxq[0]:
                    maxq.popleft()
            # print(i, j, maxq, minq)
            # update result
            res = max(res, j-i+1)
            j += 1
        return res