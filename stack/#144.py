# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def traverse(node, res):
            if node is None:
                return
            res.append(node.val)
            traverse(node.left, res)
            traverse(node.right, res)
            
        res = []
        traverse(root, res)
        return res

# iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

# advanced
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def pre(node):
            if node:
                yield node.val
                yield from pre(node.left)
                yield from pre(node.right)
                
        return list(pre(root))