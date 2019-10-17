class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        l = len(A)
        if l <= 1:
            return l
        
        left, right = 0, 1
        m = 1
        sign = None
        while right < l:
            if A[right] - A[right-1] == 0:
                m = max(m, right - left)
                left = right
                right += 1
                sign = None
                continue
            if sign is not None:
                new_sign = sign * (A[right] - A[right-1])
                if new_sign > 0:
                    m = max(m, right - left)
                    left = right - 1
            if right == l - 1:
                m = max(m, right - left + 1)
                break
            sign = A[right] - A[right-1]
            right += 1
        return m