class Solution:
    total = 0
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.helper(root, 0)
        return self.total
    
    def helper(self, node, curr):
        if node is not None:
            curr = (curr << 1) | node.val
            # sum at leaf node
            if not (node.left or node.right):
                self.total += curr
            self.helper(node.left, curr)
            self.helper(node.right, curr)
        