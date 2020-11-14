class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k = k % (m * n)
        if k:
            arr = []
            for row in grid:
                arr += row
            right = arr[-k:]
            arr[k:] = arr[:-k]
            arr[:k] = right
            grid = []
            for i in range(m):
                grid.append(arr[i*n:(i+1)*n])
        return grid
        