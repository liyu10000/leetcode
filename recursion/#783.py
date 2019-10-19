# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def pairwise(iterable):
    last = next(iterable, None)
    for item in iterable:
        yield last, item
        last = item

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def in_order(node):
            if node:
                yield from in_order(node.left)
                yield node.val
                yield from in_order(node.right)
    
        return min(b - a for a, b in pairwise(in_order(root)))