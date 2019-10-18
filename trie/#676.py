# first try: trie approach
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            node = self.root
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = None
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return self.searchWithFree(word, self.root, True)
    
    def searchWithFree(self, word, node, free):
        if node is None:
            return False
        if len(word) == 0 and '#' in node and not free:
            return True
        
        for i,char in enumerate(word):
            if not char in node:
                if free:
                    for subnode in node.values():
                        if self.searchWithFree(word[i+1:], subnode, False):
                            return True
                    return False
                else:
                    return False
            else:
                if self.searchWithFree(word[i+1:], node[char], free):
                    return True
                if free:
                    for c in node:
                        if c != char and self.searchWithFree(word[i+1:], node[c], False):
                            return True
                    return False
                return False


# second try: brute force
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for i in dict:
            self.dict[i] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz'.replace(word[i],''):
                s = word[:i]+ char + word[i+1:]
                if s in self.dict:
                    return True
        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)