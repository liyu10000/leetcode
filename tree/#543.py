class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.d = 0
        self.depth(root)
        return self.d
    
    def depth(self, node):
        if node is None:
            return 0
        leftd = 1 + self.depth(node.left)
        rightd = 1 + self.depth(node.right)
        maxd = max(leftd, rightd)
        self.d = max(self.d, leftd + rightd - 2)
        # print(node.val, maxd, self.d)
        return maxd