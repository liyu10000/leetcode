class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right = 0, 0
        m = 0
        s = 0
        for right in range(len(A)):
            s += A[right]
            if right - left + 1 - s > K:
                s -= A[left]
                left += 1
            m = max(m, right - left + 1)
        return m