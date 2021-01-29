class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        residueMap = defaultdict(int)
        pairs = 0
        for t in time:
            residue = t % 60
            if residue != 0 and residue != 30 and residueMap[60 - residue] > 0:
                pairs += residueMap[60 - residue]
            residueMap[residue] += 1
        pairs += residueMap[0] * (residueMap[0] - 1) // 2 + residueMap[30] * (residueMap[30] - 1) // 2
        # print(residueMap)
        return pairs