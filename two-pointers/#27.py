# first try
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            while slow < len(nums) and nums[slow] != val:
                slow += 1
            fast = slow + 1 if fast == 0 else fast
            while fast < len(nums) and nums[fast] == val:
                fast += 1
            if fast >= len(nums):
                return slow
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
            fast += 1
        return slow

# second try
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            while start < len(nums) and nums[start] != val:
                start += 1
            while end >= 0 and nums[end] == val:
                end -= 1
            if start >= end:
                return start
            nums[start], nums[end] = nums[end], nums[start]
        return start

# third try
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newl = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[newl] = nums[i]
                newl += 1
        return newl     