# Used a hashmap, using deque may be faster
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamps = []
        self.sumd = {}

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.timestamps and self.timestamps[-1] == timestamp:
            self.sumd[timestamp] += 1
        else:
            rmvSum = 0
            while self.timestamps and timestamp - self.timestamps[0] >= 300:
                tmp = self.timestamps.pop(0)
                del self.sumd[tmp]
            self.timestamps.append(timestamp)
            self.sumd[timestamp] = 1
        print(self.timestamps, self.sumd)
        
    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        hits = 0
        for tmp in range(timestamp-299, timestamp+1):
            if tmp in self.sumd:
                hits += self.sumd[tmp]
        return hits
