# adapted solution from #112.py and #113.py, but get TLE.
class Solution:
    cnt = 0
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def traverse(node):
            if node is None:
                return
            self.cnt += len(self.pathSum2(node, sum))
            # print(node.val, self.pathSum2(node, sum))
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return self.cnt
            
    def pathSum2(self, root: TreeNode, sum: int) -> List[List[int]]:
        def helper(node, currSum, currList):
            if node is None:
                return
            if node.val + currSum == sum:
                resLists.append(currList+[node.val])
            helper(node.left, currSum+node.val, currList+[node.val])
            helper(node.right, currSum+node.val, currList+[node.val])
            
        resLists = []
        helper(root, 0, [])
        return resLists


# a slightly faster version, able to pass
class Solution:
    cnt = 0
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def traverse(node):
            if node is None:
                return
            self.cnt += self.pathSum2(node, sum)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return self.cnt
            
    def pathSum2(self, root: TreeNode, sum: int) -> List[List[int]]:
        def helper(node, currSum):
            if node is None:
                return 0
            currCnt = 0
            if node.val + currSum == sum:
                currCnt += 1
            currCnt += helper(node.left, currSum+node.val)
            currCnt += helper(node.right, currSum+node.val)
            return currCnt
        
        return helper(root, 0)


# Best: stores path sums in a map and avoids repreated summing
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        preSum = defaultdict(int)
        preSum[0] = 1
        return self.findPathSum(root, 0, sum, preSum)
    
    def findPathSum(self, node, currSum, sum, preSum):
        if node is None:
            return 0
        # update the prefix sum by adding current val
        currSum += node.val
        # get the number of valid paths, ended by the current node
        numPathToCurr = preSum.get(currSum - sum, 0)
        # update the map with the current sum, so the map is good to be passed to the next recursion
        preSum[currSum] += 1
        # traverse left and right nodes
        res = numPathToCurr + self.findPathSum(node.left, currSum, sum, preSum) \
                            + self.findPathSum(node.right, currSum, sum, preSum)
        # restore the map, as the recursion goes from the bottom to the top
        preSum[currSum] -= 1
        return res