class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        node = root
        stack = []
        runningsum = 0
        while stack or node is not None:
            if node is not None:
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                runningsum += node.val
                node.val = runningsum
                node = node.left
        return root