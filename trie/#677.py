class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for char in key:
            node = node.setdefault(char, {})
        node['#'] = val

    def sum(self, prefix: str) -> int:
        # go to the subtree
        node = self.root
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return 0

        # sum up all vals
        stack = [node]
        s = 0
        while stack:
            node = stack.pop()
            for char in node:
                if char != '#':
                    stack.append(node[char])
                else:
                    s += node[char]
        return s
            

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)