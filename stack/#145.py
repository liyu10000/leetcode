# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def traverse(node, res):
            if node is None:
                return
            traverse(node.left, res)
            traverse(node.right, res)
            res.append(node.val)
            
        res = []
        traverse(root, res)
        return res

# iterative
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(False, root)]
        while stack:
            flag, node = stack.pop()
            if node is not None:
                if flag:
                    res.append(node.val)
                else:
                    stack.append((True, node))
                    stack.append((False, node.right))
                    stack.append((False, node.left))
        return res

# advanced
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def pre(node):
            if node:
                yield from pre(node.left)
                yield from pre(node.right)
                yield node.val
                
        return list(pre(root))