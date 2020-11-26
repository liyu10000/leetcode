class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        charIdx = defaultdict(list)
        for i,c in enumerate(S):
            charIdx[c].append(i)
        res = []
        n = len(S)
        i, j = 0, 0
        while j < n:
            # print('start', i, j)
            tmpi, tmpj = charIdx[S[i]][0], charIdx[S[i]][-1]
            cnt = len(charIdx[S[i]])
            visited = {S[tmpi]}
            while tmpj - tmpi + 1 > cnt:
                maxj = tmpj
                for k in range(tmpi+1, tmpj):
                    if not S[k] in visited:
                        maxj = max(maxj, charIdx[S[k]][-1])
                        cnt += len(charIdx[S[k]])
                        visited.add(S[k])
                tmpj = maxj
            # print('endofround', cnt, visited)
            res.append(cnt)
            i, j = tmpj+1, tmpj+1
        return res