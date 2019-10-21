class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found = 0
        for i in range(len(nums)-1, 0, -1):
            # place where we can make a change
            if nums[i-1] < nums[i]:
                found = 1
                idx = i+1 # the index of number that is the first number less than nums[i-1], hence, idx-1 is the index of smallest  number greater than nums[i-1] on the rhs.
                while idx <= len(nums)-1:
                    if nums[i-1] >= nums[idx]:
                        break
                    idx += 1
                nums[i-1], nums[idx-1] = nums[idx-1], nums[i-1] # swapping
                nums[i:] = nums[i:][::-1] # reversing the rest
                break     
        if not found:
            nums[:] = nums[::-1]