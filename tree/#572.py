# iterative
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        node = s
        stack = []
        while stack or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.val == t.val:
                    if self.isSametree(node, t):
                        return True
                node = node.right
        return False
        
    def isSametree(self, ss, tt):
        if ss is None and tt is None:
            return True
        if ss is None or tt is None:
            return False
        return ss.val == tt.val and self.isSametree(ss.left, tt.left) and self.isSametree(ss.right, tt.right)

# recursive
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.traverse(s, t)
    
    def traverse(self, s, t):
        return (s is not None) and (self.isSametree(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))
    
    def isSametree(self, ss, tt):
        if ss is None and tt is None:
            return True
        if ss is None or tt is None:
            return False
        return ss.val == tt.val and self.isSametree(ss.left, tt.left) and self.isSametree(ss.right, tt.right)