class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        for i in range(len(digits)-1):
            maxi = self.lastMaxIdx(digits[i+1:]) + i + 1
            if digits[maxi] > digits[i]:
                digits[maxi], digits[i] = digits[i], digits[maxi]
                break
        return int(''.join(digits))
    
    def lastMaxIdx(self, arr):
        maxi = len(arr) - 1
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[maxi]:
                maxi = i
        return maxi