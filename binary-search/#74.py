# O(logm + logn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        m = len(matrix)
        n = len(matrix[0])
        # locate which row to search for
        low, high = 0, m-1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        # print(low, mid, high)
        row = mid - 1 if matrix[mid][0] > target else mid
        # locate the col position in row
        left, right = 0, n-1
        while left <= right:
            center = (left + right) // 2
            if matrix[row][center] == target:
                return True
            if matrix[row][center] < target:
                left = center + 1
            else:
                right = center - 1
        # print(left, center, right)
        return False

# O(m + n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = n - 1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False