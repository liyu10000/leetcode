class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


import queue
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        qu = queue.Queue()
        qu.put((p, q))
        while not qu.empty():
            p, q = qu.get()
            if not self.same(p, q):
                return False
            if p is not None and q is not None:
                qu.put((p.left, q.left))
                qu.put((p.right, q.right))
        return True
    
    def same(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val