# recursive solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorderTraversalHelper(root, [])
        
    def inorderTraversalHelper(self, node, l):
        if node is not None:
            self.inorderTraversalHelper(node.left, l)
            l.append(node.val)
            self.inorderTraversalHelper(node.right, l)
        return l

# iterative solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        stack = []
        curr = root
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        
        while stack:
            curr = stack.pop()
            values.append(curr.val)
            curr = curr.right
            while curr is not None:
                stack.append(curr)
                curr = curr.left
        
        return values