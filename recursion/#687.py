# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longest_length = 0
        
        def helper(node):
            # if the node is None or a leaf node, return 0
            if not node: 
                return 0
            if not node.left and not node.right: 
                return 0
            # left and right are the branch values that possibly form a longer path with its prescendants; so either of them would be kept
            left = helper(node.left)
            right = helper(node.right)
            if node.left:
                # if leftnode.val == parent.val, then it's possible to form a longer path with its parent
                if node.left.val == node.val: 
                    left += 1
                else: 
                    left = 0 # already not possible to form a path with its parent, so it's OK (and necessary) to set it to 0
            if node.right:
                if node.right.val == node.val:
                    right += 1
                else: 
                    right = 0
            # if left + node + right form a non-zero path, should compare before passing the longer branch result
            self.longest_length = max(self.longest_length, left + right)
            # only pass the longer result to upper layer to see if could form longer path
            return max(left, right)
                
        helper(root)
        return self.longest_length