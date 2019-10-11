class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minid = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.stack[self.minid]:
            self.minid = len(self.stack)-1

    def pop(self) -> None:
        if self.minid == len(self.stack)-1:
            minid = 0
            for i in range(1, len(self.stack)-1):
                if self.stack[i] < self.stack[minid]:
                    minid = i
            self.minid = minid
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minid]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()