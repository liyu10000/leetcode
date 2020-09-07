# first try
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# second try
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                j += 1
                if j == len(needle):
                    return i - j + 1
            elif j != 0:
                i -= j
                j = 0
            i += 1
        return -1

# third try
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        h_len = len(haystack)
        n_len = len(needle)
        for i in range(h_len-n_len+1):
            match = True
            for j in range(n_len):
                if haystack[i+j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1

# KMP algorithm
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        table = self.buildTable(needle)
        i, j = 0, 0
        while i < len(haystack):
            while j >= 0 and haystack[i] != needle[j]:
                j = table[j]
            i += 1
            j += 1
            if j == len(needle):
                return i - len(needle)
        return -1
        
    def buildTable(self, arr):
        n = len(arr)
        table = [0 for _ in range(n+1)]
        table[0] = -1
        i, j = 0, -1
        while i < n:
            while j >= 0 and arr[i] != arr[j]:
                j = table[j]
            i += 1
            j += 1
            table[i] = j
        return table