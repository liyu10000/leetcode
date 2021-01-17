# brute force
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        double = [a * 2 for a in nums]
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > double[j]:
                    cnt += 1
        return cnt

# embed comparison with merge sort
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeWithReverse(nums, 0, len(nums)-1)
    
    def mergeWithReverse(self, nums, i, j):
        if i >= j:
            return 0
        m = (i + j) // 2
        res = self.mergeWithReverse(nums, i, m) + self.mergeWithReverse(nums, m+1, j)
        # merge sort
        p1, p2, w = i, m+1, 0
        tmp = [0] * (j-i+1)
        p = m+1 # cursor on right sub array
        c = 0   # pairs between left and right
        while p1 <= m:
            while p <= j and nums[p1] > 2 * nums[p]:
                p += 1
            c += p - (m+1)
            while p2 <= j and nums[p1] >= nums[p2]:
                tmp[w] = nums[p2]
                p2 += 1
                w += 1
            tmp[w] = nums[p1]
            p1 += 1
            w += 1
        while p2 <= j:
            tmp[w] = nums[p2]
            p2 += 1
            w += 1
        nums[i:j+1] = tmp
        # print(i, j, c, nums)
        return res + c