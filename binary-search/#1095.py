class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # find index of mountain top
        topi = self.findTop(mountain_arr)
        # search on left
        if mountain_arr.get(0) <= target <= mountain_arr.get(topi):
            li = self.incSearch(target, mountain_arr, 0, topi)
        else:
            li = -1
        # search on right
        if mountain_arr.get(topi) >= target >= mountain_arr.get(mountain_arr.length()-1):
            ri = self.decSearch(target, mountain_arr, topi, mountain_arr.length()-1)
        else:
            ri = -1
        # print(topi, li, ri)
        return li if li != -1 else ri if ri != -1 else -1
    
    def findTop(self, arr):
        l = arr.length()
        i, j = 0, l - 1
        while i <= j:
            mid = i + (j - i) // 2
            lnum = arr.get(mid-1)
            mnum = arr.get(mid)
            rnum = arr.get(mid+1)
            if lnum < mnum < rnum:
                i = mid
            elif lnum > mnum > rnum:
                j = mid
            else:
                return mid
        return -1
    
    def incSearch(self, target, arr, i, j):
        while i <= j:
            mid = i + (j - i) // 2
            num = arr.get(mid)
            if num == target:
                return mid
            elif num < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1
    
    def decSearch(self, target, arr, i, j):
        while i <= j:
            mid = i + (j - i) // 2
            num = arr.get(mid)
            if num == target:
                return mid
            elif num > target:
                i = mid + 1
            else:
                j = mid - 1
        return -1