# use an array to mark occurrence
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        a = [0] * 1441 # 24 * 60 = 1440
        mini, maxi = 1441, 0
        for t in timePoints:
            hh, mm = int(t[:2]), int(t[3:])
            i = hh*60+mm if hh != 0 or mm != 0 else 1440
            mini = min(mini, i)
            maxi = max(maxi, i)
            # print(i)
            a[i] += 1
        md = 1440 - maxi + mini
        i = 1
        if a[1440] > 1:
            return 0
        while i < 1440:
            # print(i)
            if a[i] > 1:
                return 0
            elif a[i] > 0:
                for j in range(i+1, 1441):
                    if a[j] > 0:
                        break
                if a[j] > 0:
                    md = min(md, j - i)
                i = j
            else:
                i += 1
        return md