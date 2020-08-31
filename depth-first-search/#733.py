class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visited = set()
        self.fill(image, visited, m, n, sr, sc, image[sr][sc], newColor)
        return image
        
    def fill(self, image, visited, m, n, i, j, color, newColor):
        image[i][j] = newColor
        visited.add((i,j))
        for r,c in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
            if 0 <= r < m and 0 <= c < n and image[r][c] == color and not (r,c) in visited:
                self.fill(image, visited, m, n, r, c, color, newColor)