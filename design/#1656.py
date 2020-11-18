class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 1
        self.d = defaultdict(str)

    def insert(self, id: int, value: str) -> List[str]:
        self.d[id] = value
        res = []
        if self.d[self.ptr]:
            for ptr in range(self.ptr, self.n+1):
                if self.d[ptr]:
                    res.append(self.d[ptr])
                else:
                    break
            self.ptr = ptr
        return res