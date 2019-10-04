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