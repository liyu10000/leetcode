class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        
class Circle:
    def __init__(self, n):
        self.n = n
        self.c = n
        self.form_circle()
        
    def get_head(self):
        return self.head.val
    
    def get_nodes(self):
        return self.c
    
    def form_circle(self):
        head = Node(1)
        curr = head
        for i in range(2, self.n+1):
            curr.next = Node(i)
            curr.next.prev = curr
            curr = curr.next
        curr.next = head
        head.prev = curr
        self.head = head
    
    def remove_node(self, k):
        curr = self.head
        for _ in range(1, k):
            curr = curr.next
        prev = curr.prev
        prev.next = curr.next
        curr.next.prev = prev
        curr = prev.next
        self.c -= 1
        self.head = curr

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1 or n == 1:
            return n
        circle = Circle(n)
        while circle.get_nodes() > 1:
            circle.remove_node(k)
        return circle.get_head()