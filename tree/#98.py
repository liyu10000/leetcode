class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        values = []
        stack = []
        curr = root
        while curr is not None:
            stack.append(curr)
            curr = curr.left
            
        while stack:
            curr = stack.pop()
            if values and values[-1] >= curr.val:
                return False
            else:
                values.append(curr.val)
            curr = curr.right
            while curr is not None:
                stack.append(curr)
                curr = curr.left
        
        return True