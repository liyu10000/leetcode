# The basic idea is to find zero values and check nonzero values between them. If the number of negative values is odd in a segment, then check the products in a reverse order. During the traversal, need to track the index of zero values so that we can check the segment in between.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPro, curPro = float('-inf'), 1
        zeroIdx, negCnt = -1, 0 # zero value index and negative value count
        for i in range(len(nums)):
            if nums[i] == 0:
                maxPro = max(maxPro, 0)
                if negCnt % 2 == 1:  # reverse array and check products
                    curPro = 1
                    for j in range(i-1, zeroIdx, -1):
                        curPro *= nums[j]
                        maxPro = max(maxPro, curPro)
                curPro = 1
                zeroIdx = i
                negCnt = 0
            else:
                if nums[i] < 0:
                    negCnt += 1
                curPro *= nums[i]
                maxPro = max(maxPro, curPro)
        
        # check the last segment after the last zero value
        if negCnt % 2 == 1:
            curPro = 1
            for j in range(i, zeroIdx, -1):
                curPro *= nums[j]
                maxPro = max(maxPro, curPro)
                
        return maxPro


# dp, can be simplified with O(1) space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        minp = [0] * n
        maxp = [0] * n
        minp[0] = maxp[0] = nums[0]
        res = maxp[0]
        for i in range(1, n):
            minp[i] = min(nums[i], min(minp[i-1]*nums[i], maxp[i-1]*nums[i]))
            maxp[i] = max(nums[i], max(minp[i-1]*nums[i], maxp[i-1]*nums[i]))
            res = max(maxp[i], res)
        return res