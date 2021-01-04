class CustomStack:

    def __init__(self, maxSize: int):
        self.s = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.s) < self.maxSize:
            self.s.append(x)

    def pop(self) -> int:
        if self.s:
            return self.s.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.s))
        for i in range(k):
            self.s[i] += val


# better approach
class CustomStack:

    def __init__(self, maxSize: int):
        self.s = []
        self.inc = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.inc) < self.maxSize:
            self.s.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.inc:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.s.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc))-1] += val