class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if k == 1: return True
        residue = defaultdict(int)
        for a in arr:
            a = a % k
            if a == 0 or a == k-a:
                if residue[a] > 0:
                    residue[a] -= 1
                else:
                    residue[a] += 1
            else:
                if k - a in residue:
                    residue[k-a] -= 1
                else:
                    residue[a] += 1
        # print(residue)
        for a,c in residue.items():
            if c != 0:
                return False
        return True