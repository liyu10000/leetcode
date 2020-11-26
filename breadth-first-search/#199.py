# BFS
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            res.append(queue[-1].val)
            newqueue = []
            for node in queue:
                if node.left is not None:
                    newqueue.append(node.left)
                if node.right is not None:
                    newqueue.append(node.right)
            queue = newqueue
        return res

# DFS
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        
        def dfs(node, level):
            if level == len(res):
                res.append(node.val)
            if node.right:
                dfs(node.right, level+1)
            if node.left:
                dfs(node.left, level+1)
        
        dfs(root, 0)
        return res