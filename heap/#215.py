# first try
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]

# second try: different strategies of using heapq
def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        return heapq.heappop(nums)
#     ---------------------------------------------------------
    
        ans = []
        for i in nums:
            heapq.heappush(ans, i)
            if len(ans)>k:
                heapq.heappop(ans)
        
        return heapq.heappop(ans)
#     ---------------------------------------------------------
    
        return heapq.nlargest(k, nums)[-1]