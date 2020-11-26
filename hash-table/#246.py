class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dmap = {'1':'1', '6':'9', '8':'8', '9':'6', '0':'0'}
        newnum = ''
        for c in num:
            if c in dmap:
                newnum += dmap[c]
            else:
                return False
        newnum = newnum[::-1]
        # print(newnum)
        return num == newnum