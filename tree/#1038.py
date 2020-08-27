# same to problem 538
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        node = root
        stack = []
        runningsum = 0
        while stack or node is not None:
            if node is not None:
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                runningsum += node.val
                node.val = runningsum
                node = node.left
        return root


class Solution:
    carry = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.traversal(root)
        return root
    
    def traversal(self, node):
        if node is None:
            return
        self.traversal(node.right)
        self.carry += node.val
        node.val = self.carry
        self.traversal(node.left)