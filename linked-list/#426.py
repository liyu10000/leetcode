class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def inorder(node):
            nonlocal first, last
            if node:
                inorder(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                inorder(node.right)
        if not root:
            return None
        first, last = None, None
        inorder(root)
        last.right = first
        first.left = last
        return first