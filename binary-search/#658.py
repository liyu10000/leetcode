# Two-step solution
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = self.findIndex(arr, x)
        l, r = i, i
        while r - l < k:
            if l == 0: return arr[:k]
            if r == len(arr): return arr[-k:]
            if x - arr[l-1] <= arr[r] - x: 
                l -= 1
            else: 
                r += 1
        return arr[l:r]
        
    def findIndex(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

# One-step solution
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]