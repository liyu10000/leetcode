# O(n) time and O(n) space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        flag = [-1] * (n+1)
        for num in nums:
            if 1 <= num <= n:
                flag[num] = num
        # print(flag[1:])
        for num in range(1, n+1):
            if flag[num] == -1:
                return num
        return n+1

# O(n) time and O(1) space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                # print(nums)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1