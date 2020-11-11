class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        root.par = None
        self.dfs(root) # dfs to get parent node for each node
        return self.bfs(target, K) # bfs to find nodes at distance K from target node
    
    def dfs(self, root):
        if root is None:
            return
        if root.left:
            root.left.par = root
            self.dfs(root.left)
        if root.right:
            root.right.par = root
            self.dfs(root.right)
            
    def bfs(self, target, K):
        visited = set()
        step = 0
        queue = [target]
        while queue:
            if step == K:
                break
            step += 1
            newqueue = []
            for node in queue:
                visited.add(node.val)
                for subnode in [node.par, node.left, node.right]:
                    if subnode and not subnode.val in visited:
                        newqueue.append(subnode)
            queue = newqueue
        return [node.val for node in queue]