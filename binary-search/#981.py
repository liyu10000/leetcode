class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.d:
            return ""
        l = self.d[key]
        i = self.binarySearch(l, timestamp)
        return '' if i == 0 else l[i-1][1]
    
    def binarySearch(self, l, t):
        first = 0
        last = len(l)
        while first < last:
            mid = (first + last)//2
            if t < l[mid][0]:
                last = mid
            else:
                first = mid + 1 
        return last