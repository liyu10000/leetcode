"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

# first try
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        nodedict = {}
        currnode = head
        while currnode:
            nodedict[currnode] = Node(currnode.val, None, None)
            currnode = currnode.next
            
        currnode = head
        while currnode:
            if currnode.next:
                nodedict[currnode].next = nodedict[currnode.next]
            if currnode.random:
                nodedict[currnode].random = nodedict[currnode.random]
            currnode = currnode.next
        
        return nodedict[head]


# second try
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        nodedict = {}
        def helper(node):
            if node:
                if node in nodedict:
                    return nodedict[node]
                else:
                    curr = Node(node.val, None, None)
                    nodedict[node] = curr
                    curr.next = helper(node.next)
                    curr.random = helper(node.random)
                    return curr
            else:
                return None
        return helper(head)