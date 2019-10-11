# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
        return res[::-1]