# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            c = len(nums) // 2
            node = TreeNode(nums[c])
            node.left = self.sortedArrayToBST(nums[:c])
            node.right = self.sortedArrayToBST(nums[c+1:])
            return node