# first try: divide and conquer, lengthy answer
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        return self.search(matrix, target, 0, len(matrix)-1, 0, len(matrix[0])-1)
    
    def searchLine(self, array, target):
        i, j = 0, len(array)-1
        while i <= j:
            mid = i + (j-i)//2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False
    
    def search(self, matrix, target, mi, mj, ni, nj):
        # print(mi, mj, ni, nj)
        if mi == mj:
            return self.searchLine(matrix[mi][ni:nj+1], target)
        if ni == nj:
            return self.searchLine([matrix[k][ni] for k in range(mi, mj+1)], target)
        
        m = mj - mi
        n = nj - ni
        if m > n:
            return self.search(matrix, target, mi, mi+n, ni, nj) or self.search(matrix, target, mi+n+1, mj, ni, nj)
        elif m < n:
            return self.search(matrix, target, mi, mj, ni, ni+m) or self.search(matrix, target, mi, mj, ni+m+1, nj)
        else:
            mmid = mi + m // 2
            nmid = ni + n // 2
            if matrix[mmid][nmid] > target:
                return self.search(matrix, target, mi, mmid, ni, nmid) or self.search(matrix, target, mmid+1, mj, ni, nmid-1) or self.search(matrix, target, mi, mmid-1, nmid+1, nj)
            elif matrix[mmid][nmid] < target:
                return self.search(matrix, target, mmid+1, mj, ni, nmid) or self.search(matrix, target, mi, mmid, nmid+1, nj) or self.search(matrix, target, mmid+1, mj, nmid+1, nj)
            else:
                return True


# second try
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1
        while  i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False