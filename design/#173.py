# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# flatten beforehead
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.index = 0
        self.nodeSorted = []
        self._inorder(root)
        
    def _inorder(self, root: TreeNode):
        if root is None:
            return
        self._inorder(root.left)
        self.nodeSorted.append(root.val)
        self._inorder(root.right)
        
    def _inorderIterative(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
            
        while self.stack:
            node = self.stack.pop()
            self.nodeSorted.append(node.val)
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        val = self.nodeSorted[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.nodeSorted)


# controlled traversal
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._inorder_left(root)
        
    def _inorder_left(self, node: TreeNode):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        self._inorder_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()