class LargerNum(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=LargerNum)
        # print(nums)
        return ''.join(nums) if nums[0] != '0' else '0'