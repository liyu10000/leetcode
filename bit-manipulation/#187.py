class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        a = set()
        res = set()
        for i in range(len(s)-9):
            if s[i:i+10] in a:
                res.add(s[i:i+10])
            a.add(s[i:i+10])
        return res