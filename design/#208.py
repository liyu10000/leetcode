class Node:
    def __init__(self, val):
        self.val = val
        self.isWord = False
        self.children = {}  # stores the val of children

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        node.isWord = True
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)