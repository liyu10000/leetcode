# brute force
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n in nums1:
            i = nums2.index(n)
            nextGreat = n
            for j in range(i+1, len(nums2)):
                if nums2[j] > n:
                    nextGreat = nums2[j]
                    break
            nextGreat = nextGreat if nextGreat > n else -1
            res.append(nextGreat)
        return res

# Stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        d = {}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                d[stack.pop()] = n
            stack.append(n)
        for n in nums1:
            res.append(d.get(n, -1))
        return res