# Math solution, not line sweep
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        pointSet = set()
        area = 0
        for rec in rectangles:
            bottom_left = (rec[0], rec[1])
            bottom_right = (rec[2], rec[1])
            top_left = (rec[0], rec[3])
            top_right = (rec[2], rec[3])
            for p in [bottom_left, bottom_right, top_left, top_right]:
                if p in pointSet:
                    pointSet.remove(p)
                else:
                    pointSet.add(p)
            area += (rec[2] - rec[0]) * (rec[3] - rec[1])
        if len(pointSet) != 4:
            return False
        pointSet = sorted(pointSet)
        p1 = pointSet.pop(0)
        p2 = pointSet.pop()
        return area == (p2[0] - p1[0]) * (p2[1] - p1[1])