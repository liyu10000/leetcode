class Solution:
    ctarget = None
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.getTarget(original, cloned, target)
        return self.ctarget
    
    def getTarget(self, original, cloned, target):
        if original is None and target is not None:
            return False
        if original == target:
            self.ctarget = cloned
            return True
        
        return self.getTarget(original.left, cloned.left, target) \
            or self.getTarget(original.right, cloned.right, target)