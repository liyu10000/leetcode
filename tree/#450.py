class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            else:
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                root.val = tmp.val
                root.left = self.deleteNode(root.left, tmp.val)
        return root

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.right is None:
                return root.left
            else:
                tmp = root.right
                while tmp.left:
                    tmp = tmp.left
                root.val = tmp.val
                root.right = self.deleteNode(root.right, tmp.val)
        return root