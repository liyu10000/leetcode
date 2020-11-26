class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S
        charCnt = defaultdict(int)
        for c in S:
            charCnt[c] += 1
        pq = []
        for c,cnt in charCnt.items():
            heapq.heappush(pq, (-cnt, c))
        # print(pq)
        s = ''
        while len(pq) > 1:
            cnt1, char1 = heapq.heappop(pq)
            cnt2, char2 = heapq.heappop(pq)
            s += char1 + char2
            if cnt1 < -1:
                heapq.heappush(pq, (cnt1+1, char1))
            if cnt2 < -1:
                heapq.heappush(pq, (cnt2+1, char2))
            # print(s, pq)
        if pq:
            cnt, char = heapq.heappop(pq)
            if cnt == -1:
                s += char
            else:
                return ''
        return s