class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        # get parent node, the depth
        self.parents = {root.val:[root.val, 0]} # parent val
        self.traverse(root, 0)
        # print(self.parents)
        # find common parent
        pdepth = 0
        qdepth = 0
        while p != q:
            if self.parents[p][1] > self.parents[q][1]:
                p = self.parents[p][0]
                pdepth += 1
            elif self.parents[p][1] < self.parents[q][1]:
                q = self.parents[q][0]
                qdepth += 1
            else:
                p = self.parents[p][0]
                q = self.parents[q][0]
                pdepth += 1
                qdepth += 1
        # print(pdepth, qdepth)
        return pdepth + qdepth
        
    def traverse(self, root, depth):
        depth += 1
        if root.left:
            self.parents[root.left.val] = [root.val, depth]
            self.traverse(root.left, depth)
        if root.right:
            self.parents[root.right.val] = [root.val, depth]
            self.traverse(root.right, depth)