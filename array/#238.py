class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = self.product(nums)
        backward = self.product(nums[::-1])[::-1]
        return [f*b for f,b in zip(forward, backward)]
    
    def product(self, nums):
        ps = []
        for i,n in enumerate(nums):
            if i == 0:
                ps.append(1)
            else:
                ps.append(nums[i-1] * ps[-1])
        # print(ps)
        return ps