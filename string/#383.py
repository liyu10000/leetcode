class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        rd = defaultdict(int)
        md = defaultdict(int)
        for c in magazine:
            md[c] += 1
        for c in ransomNote:
            rd[c] += 1
            if c not in md or rd[c] > md[c]:
                return False
        return True