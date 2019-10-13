"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        queue = deque([node])
        table = {node:Node(node.val, [])}
        
        while queue:
            currNode = queue.popleft()
            for n in currNode.neighbors:
                if n not in table:
                    newNode = Node(n.val, [])
                    table[n] = newNode
                    queue.append(n)
                table[currNode].neighbors.append(table[n])
                
        return table[node]