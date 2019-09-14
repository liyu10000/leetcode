class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        area = -1
        while i < j:
            left, right = height[i], height[j]
            h = min(left, right)
            area = max(area, (j - i) * h)
            if left > right:
                j -= 1
            else:
                i += 1
        return area