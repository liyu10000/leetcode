# naive solution, time limit exceeded
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        k = k % len_
        for i in range(k):
            tmp = nums[-1]
            for j in range(len_-1, 0, -1):
                nums[j-1], nums[j] = nums[j-2], nums[j-1]
            nums[0] = tmp

# solution 2, O(n) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        k = k % len_
        tmp = nums[len_ - k:]
        for i in range(len_ - k - 1, -1, -1):
            nums[i + k] = nums[i]
        for i in range(k):
            nums[i] = tmp[i]

# solution 3, O(1) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        k = k % len_
        self.reverse(nums, 0, len_ - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len_ - 1)
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1