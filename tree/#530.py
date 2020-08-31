class Solution:
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        vals = []
        self.traversal(root, vals)
        # print(vals)
        # vals.sort()
        l = len(vals)
        diff = 2**32
        for i in range(l-1):
            if vals[i+1] - vals[i] < diff:
                diff = vals[i+1] - vals[i]
        return diff
    
    def traversal(self, node, vals):
        if node.left is not None:
            self.traversal(node.left, vals)
        vals.append(node.val)
        if node.right is not None:
            self.traversal(node.right, vals)