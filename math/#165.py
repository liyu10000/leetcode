class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # find number of dots in two strings, pad short to match long
        cnt1 = version1.count('.')        
        cnt2 = version2.count('.')
        if cnt1 < cnt2:
            version1 += '.0' * (cnt2 - cnt1)
        else:
            version2 += '.0' * (cnt1 - cnt2)
        # compare each version number, from left to right
        len1 = len(version1)
        len2 = len(version2)
        i, j = 0, 0
        for cnt in range(max(cnt1, cnt2)+1):
            ii = version1.find('.', i)
            jj = version2.find('.', j)
            ii = len(version1) if ii == -1 else ii
            jj = len(version2) if jj == -1 else jj
            if int(version1[i:ii]) > int(version2[j:jj]):
                return 1
            elif int(version1[i:ii]) < int(version2[j:jj]):
                return -1
            else:
                i = ii + 1
                j = jj + 1
        return 0

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # split str
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        # compare each version number
        cnt1 = len(nums1)
        cnt2 = len(nums2)
        for i in range(max(cnt1, cnt2)):
            n1 = int(nums1[i]) if i < cnt1 else 0
            n2 = int(nums2[i]) if i < cnt2 else 0
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        return 0
        