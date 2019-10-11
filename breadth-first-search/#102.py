# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# first try
import queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q1, q2 = queue.Queue(), queue.Queue()
        q1.put(root)
        while True:
            r = []
            while not q1.empty():
                node = q1.get()
                r.append(node.val)
                if node.left:
                    q2.put(node.left)
                if node.right:
                    q2.put(node.right)
            res.append(r)
            if q2.empty():
                break
            q1, q2 = q2, q1
        return res


# second try
import queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            r = []
            for _ in range(size):
                node = q.get()
                r.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            res.append(r)
        return res


# third try:
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:        
        def helper(node, res, i):
            if node is None:
                return 
            if i == len(res):
                res.append([])
            res[i].append(node.val)
            helper(node.left, res, i+1)
            helper(node.right, res, i+1)
        
        res = []
        helper(root, res, 0)
            
        return res