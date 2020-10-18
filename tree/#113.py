class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def helper(node, currSum, currList):
            if node is None:
                return
            if node.left is None and node.right is None and node.val + currSum == sum:
                resLists.append(currList+[node.val])
                return
            helper(node.left, currSum+node.val, currList+[node.val])
            helper(node.right, currSum+node.val, currList+[node.val])
            
        resLists = []
        helper(root, 0, [])
        return resLists