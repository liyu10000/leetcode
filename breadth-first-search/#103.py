# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def helper(node, res, i):
            if node is None:
                return
            if i == len(res):
                res.append([])
            if i % 2 == 0:
                res[i].append(node.val)
            else:
                res[i] = [node.val] + res[i]
            helper(node.left, res, i+1)
            helper(node.right, res, i+1)
            
        res = []
        helper(root, res, 0)

        return res