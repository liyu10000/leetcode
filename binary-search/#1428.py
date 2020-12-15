# binary search each row
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        
        def search(row, i, j):
            while i < j:
                mid = (i + j) // 2
                if binaryMatrix.get(row, mid):
                    j = mid
                else:
                    i = mid + 1
            return j if binaryMatrix.get(row, j) else cols
        
        leftmost = cols
        for row in range(rows):
            mid = search(row, 0, cols-1)
            leftmost = min(leftmost, mid)
        return leftmost if leftmost != cols else -1

# optimized: binary search each row and update search ending point
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        
        def search(row, i, j):
            while i < j:
                mid = (i + j) // 2
                if binaryMatrix.get(row, mid):
                    j = mid
                else:
                    i = mid + 1
            return j if binaryMatrix.get(row, j) else cols
        
        leftmost = cols
        for row in range(rows):
            mid = search(row, 0, leftmost-1)
            leftmost = min(leftmost, mid)
            if leftmost == 0:
                return 0
        return leftmost if leftmost != cols else -1