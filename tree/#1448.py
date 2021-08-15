class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        
        def dfs(node, val):
            if val <= node.val:
                val = node.val
                self.cnt += 1
            if node.left:
                dfs(node.left, val)
            if node.right:
                dfs(node.right, val)
        
        dfs(root, root.val)
        return self.cnt