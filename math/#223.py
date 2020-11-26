class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        overlap = self.getOverlap(A,B,C,D,E,F,G,H)
        return area1 + area2 - overlap
    
    def getOverlap(self, A,B,C,D,E,F,G,H):
        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)
        if x2 > x1 and y2 > y1:
            return (x2 - x1) * (y2 - y1)
        else:
            return 0