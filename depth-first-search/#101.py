class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
    
    def compare(self, l, r):
        if l is None and r is None:
            return True
        elif l is None or r is None:
            return False
        else:
            if l.val != r.val:
                return False
            else:
                return self.compare(l.left, r.right) and self.compare(l.right, r.left)