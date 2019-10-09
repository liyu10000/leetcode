# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        elif len(preorder) == 0:
            return None
        
        i, val = 0, preorder[0]
        while val != inorder[i]:
            i += 1
        i += 1
        
        node = TreeNode(val)
        node.left = self.buildTree(preorder[1:i], inorder[:i-1])
        node.right = self.buildTree(preorder[i:], inorder[i:])
        return node
        
