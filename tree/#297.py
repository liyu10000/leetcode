# Store and retrieve in BFS order, keep null in string, get TLE
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.data = ''
        
        def bfs(node):
            q = [root]
            while q:
                nonzero = False
                newq = []
                for i, node in enumerate(q):
                    if node is None:
                        self.data += ',n'
                        newq.append(None)
                        newq.append(None)
                    else:
                        self.data += ',' + str(node.val)
                        if node.left or node.right:
                            nonzero = True
                        newq.append(node.left)
                        newq.append(node.right)
                q = newq if nonzero else []
        
        bfs(root)
        # print(self.data[1:])
        return self.data[1:]
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tokens = data.split(',')
        
        if tokens[0] == 'n':
            return None
        root = TreeNode(int(tokens[0]))
        i = 1
        q = [root]
        # build binary tree layer by layer
        while i < len(tokens):
            newq = []
            for node in q:
                if node is None:
                    newq.append(None)
                    newq.append(None)
                else:
                    node.left = TreeNode(int(tokens[i])) if tokens[i] != 'n' else None
                    node.right = TreeNode(int(tokens[i+1])) if tokens[i+1] != 'n' else None
                    newq.append(node.left)
                    newq.append(node.right)
                i += 2
            q = newq
        return root


# read and retrieve in dfs order
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if node:
                vals.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                vals.append('n')
        vals = []
        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            val = next(vals)
            if val == 'n':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        vals = iter(data.split(','))
        return dfs()
