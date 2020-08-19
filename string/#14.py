class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        # strs.sort() # not neccessary
        a = strs[0]
        res = ''
        for c in a:
            for i in range(1, len(strs)):
                if not strs[i].startswith(res+c):
                    return res
            res += c
        return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_cnt = len(strs)
        if str_cnt == 0:
            return ""
        elif str_cnt == 1:
            return strs[0]
        min_len = min([len(s) for s in strs])
        i = 0
        while i < min_len:
            c = strs[0][i]
            for j in range(1, str_cnt):
                if c != strs[j][i]:
                    return strs[0][:i]
            i += 1
        if i == min_len:
            return strs[0][:i]
        else:
            return ""