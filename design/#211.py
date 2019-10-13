class Node:
    def __init__(self, val):
        self.val = val
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            if not c in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        node.isWord = True
        
    def _search(self, word, node) -> bool:
        if not word:
            return node.isWord
        childList = []
        if word[0] == '.':
            childList = node.children
        elif word[0] in node.children:
            childList = [word[0]]
        for child in childList:
            if self._search(word[1:], node.children[child]):
                return True
        return False

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)