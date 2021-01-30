# brute force search
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0] * n
        preSum[0] = nums[0]
        for i in range(1, n):
            preSum[i] = preSum[i-1] + nums[i]
        res = 0
        i, j = 0, 0
        for i in range(n-2):
            if preSum[i] * 3 <= preSum[n-1]:
                for j in range(i+1, n-1):
                    if preSum[j] - preSum[i] > preSum[n-1] - preSum[j]:
                        break
                    if preSum[i] <= preSum[j] - preSum[i] <= preSum[n-1] - preSum[j]:
                        res += 1
        return res % (10**9 + 7)

# binary search
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9+7
        presum = [0]*(n+1)
        for i in range(n):
            presum[i+1] = presum[i]+nums[i]

        def binarySearchLeft(i, target):
            # in nums[i+1:n-1] find the min j s.t.
            # nums[i+1]+...+nums[j] >= target
            left = i+1
            right = n-2
            while left < right:
                mid = (left+right)//2
                current = presum[mid+1]-presum[i+1]
                if current >= target:
                    right = mid
                else:
                    left = mid+1
            return left

        def binarySearchRight(i, target):
            # in nums[i+1:n-1] find the max j s.t.
            # nums[i+1]+...+nums[j] <= target
            left = i+1
            right = n-2
            while left < right:
                mid = (left+right)//2+1
                current = presum[mid+1]-presum[i+1]
                if current > target:
                    right = mid-1
                else:
                    left = mid
            return left

        result = 0
        for i in range(n-2):
            # nums[0],...,nums[i] | nums[i+1], nums[i+2], ...
            leftSum = presum[i+1]
            remain = presum[n]-leftSum
            if remain < leftSum*2:
                break
            first = binarySearchLeft(i, leftSum)
            last = binarySearchRight(i, remain//2)
            result += max(last-first+1, 0)

        return result % MOD