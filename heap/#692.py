# using hashmap
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # word: count
        d = defaultdict(int)
        for w in words:
            d[w] += 1
        # print(d)
        # count: word list
        dd = defaultdict(list)
        for w,c in d.items():
            dd[c].append(w)
        # sort by count
        od = sorted(dd.items(), reverse=True)
        # print(od)
        res = []
        for c, ws in od:
            if k == 0:
                break
            ws.sort()
            if k >= len(ws):
                res += ws
                k -= len(ws)
            else:
                res += ws[:k]
                break
        return res

# heap
class Solution:
    def topKFrequent(self, words: 'List[str]', k: 'int') -> 'List[str]':
        Freqs = collections.Counter(words)
        return heapq.nsmallest(k, Freqs,
            key=lambda word:(-Freqs[word], word)
        )