# Use hashset
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        s = set()
        for n in nums:
            if n in s:
                duplicates.append(n)
            else:
                s.add(n)
        return duplicates

# Use the array as a hashset
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                duplicates.append(abs(n))
            else:
                nums[abs(n)-1] *= -1
        return duplicates