# remember all indices, get TLE
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        d = defaultdict(list)
        for i,t in enumerate(T):
            d[t].append(i)
        res = []
        for i,t in enumerate(T):
            mini = len(T)
            for tt in range(t+1, 101):
                if tt in d:
                    for ii in d[tt]:
                        if i < ii < mini:
                            mini = ii
                            break
            res.append(mini-i if mini != len(T) else 0)
        return res

# use stack
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        s = []
        res = [0 for _ in range(len(T))]
        for i,t in enumerate(T):
            while s and s[-1][0] < t:
                tt,ii = s.pop()
                res[ii] = i - ii
            s.append([t, i])
        return res

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        s = []
        res = [0] * len(T)
        for i,t in enumerate(T):
            while s and T[s[-1]] < t:
                ii = s.pop()
                res[ii] = i - ii
            s.append(i)
        return res