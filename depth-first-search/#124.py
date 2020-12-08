class Solution:
    m = -1000
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.m
        
    def helper(self, root):
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        m = max(root.val, root.val+left, root.val+right)
        self.m = max(self.m, m, root.val+left+right)
        return m