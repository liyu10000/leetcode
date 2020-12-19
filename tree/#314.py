class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        self.d = defaultdict(list)
        self.traverse(root, 0, 0)
        res = []
        xs = list(self.d.keys())
        xs.sort()
        for x in xs:
            jvals = self.d[x]
            jvals.sort(key=lambda i:i[0])
            res.append([i[1] for i in jvals])
        return res
        
    def traverse(self, node, i, j):
        if node is None:
            return
        self.d[i].append([-j, node.val])
        self.traverse(node.left, i-1, j-1)
        self.traverse(node.right, i+1, j-1)