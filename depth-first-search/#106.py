# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 1:
            return TreeNode(postorder[0])
        elif len(postorder) == 0:
            return None
        
        i, val = -1, postorder[-1]
        while val != inorder[i]:
            i -= 1
        
        node = TreeNode(val)
        node.left = self.buildTree(inorder[:i], postorder[:i])
        node.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return node