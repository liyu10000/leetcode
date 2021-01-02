# use two stacks
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # build increasing stack
        n = len(nums)
        lstack = []
        for i in range(n):
            while lstack and nums[lstack[-1]] > nums[i]:
                lstack.pop()
            lstack.append(i)
        # print(lstack)
        if len(lstack) == n: # ordered
            return 0
        # build decreasing stack
        rstack = []
        for i in range(n-1, -1, -1):
            while rstack and nums[rstack[-1]] < nums[i]:
                rstack.pop()
            rstack.append(i)
        # print(rstack)
        # find left and right index where order ends
        valid = set(lstack) & set(rstack)
        l, r = 0, 0
        for i in range(n):
            if not i in valid:
                l = i
                break
        for i in range(n-1, -1, -1):
            if not i in valid:
                r = i
                break
        return r - l + 1

# simplified two stacks
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = n-1, 0
        # build increasing stack
        lstack = []
        for i in range(n):
            while lstack and nums[lstack[-1]] > nums[i]:
                l = min(l, lstack.pop())
            lstack.append(i)
        # print(lstack)
        if len(lstack) == n: # ordered
            return 0
        # build decreasing stack
        rstack = []
        for i in range(n-1, -1, -1):
            while rstack and nums[rstack[-1]] < nums[i]:
                r = max(r, rstack.pop())
            rstack.append(i)
        # print(rstack)
        return r - l + 1

# sort array
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = n-1, 0
        copy = nums[:]
        copy.sort()
        for i in range(n):
            if copy[i] != nums[i]:
                l = i
                break
        for i in range(n-1, -1, -1):
            if copy[i] != nums[i]:
                r = i
                break
        return r - l + 1 if l < r else 0