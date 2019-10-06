# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        if n < 1:
            return []
        
        def generate(lo, hi):
            if lo > hi:
                return [None]
            elif lo == hi:
                return [TreeNode(lo)]
            else:
                res = []
                for i in range(lo, hi+1):
                    ll = generate(lo, i-1)
                    rr = generate(i+1, hi)
                    for l in ll:
                        for r in rr:
                            node = TreeNode(i)
                            node.left = l
                            node.right = r
                            res.append(node)
                return res
            
        return generate(1, n)

def printTrees(root):
    if root is not None:
        printTrees(root.left)
        print(root.val, end=' ')
        printTrees(root.right)
    else:
        print('null', end=' ')


if __name__ == '__main__':
    s = Solution()
    l = s.generateTrees(3)
    for t in l:
        printTrees(t)
        print()
