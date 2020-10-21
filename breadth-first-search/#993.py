# naive bfs
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.xd = [-1, -1]
        self.yd = [-1, -1]
        self.bfs(root, x, y, 0)
        # print(self.xd, self.yd)
        return self.xd[0] != self.yd[0] and self.xd[1] == self.yd[1]
        
    def bfs(self, node, x, y, depth):
        if node is None:
            return
        if node.left is None and node.right is None:
            return
        if node.left is not None:
            if node.left.val == x:
                self.xd = [node.val, depth+1]
            if node.left.val == y:
                self.yd = [node.val, depth+1]
            self.bfs(node.left, x, y, depth+1)
        if node.right is not None:
            if node.right.val == x:
                self.xd = [node.val, depth+1]
            if node.right.val == y:
                self.yd = [node.val, depth+1]
            self.bfs(node.right, x, y, depth+1)

