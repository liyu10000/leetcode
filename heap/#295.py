# brute force heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.q, num)

    def findMedian(self) -> float:
        hold = []
        n = len(self.q)
        for i in range(n//2+1):
            hold.append(heapq.heappop(self.q))
        if n % 2 == 0:
            median = (hold[-2] + hold[-1]) / 2
        else:
            median = hold[-1]
        for num in hold:
            heapq.heappush(self.q, num)
        return median


# use two heaps
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minq = [] # store in increasing order
        self.maxq = [] # store in decreasing order

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxq, -heapq.heappushpop(self.minq, num))
        if len(self.maxq) > len(self.minq):
            heapq.heappush(self.minq, -heapq.heappop(self.maxq))
        # print(self.maxq, self.minq)

    def findMedian(self) -> float:
        if len(self.maxq) == len(self.minq):
            return (-self.maxq[0] + self.minq[0]) / 2
        else:
            return self.minq[0]