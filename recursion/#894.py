# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        else:
            res = []
            for i in range(1, N-1, 2):
                leftList = self.allPossibleFBT(i)
                rightList = self.allPossibleFBT(N-1-i)
                for left in leftList:
                    for right in rightList:
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        res.append(node)
            return res