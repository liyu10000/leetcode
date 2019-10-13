# two queues
from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1) > 1:
            item = self.q1.popleft()
            self.q2.append(item)
        item = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return item
        

    def top(self) -> int:
        """
        Get the top element.
        """
        while self.q1:
            item = self.q1.popleft()
            self.q2.append(item)
        self.q1, self.q2 = self.q2, self.q1
        return item
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1


# one queue with count
from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.n = 0
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        self.n += 1
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(self.n-1):
            self.q.append(self.q.popleft())
        self.n -= 1
        return self.q.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        for i in range(self.n):
            item = self.q.popleft()
            self.q.append(item)
        return item
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.n == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
