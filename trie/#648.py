class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        # build trie
        root = {}
        for word in dict:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word
        
        # replace with root words
        words = sentence.split()
        new_words = []
        for word in words:
            node = root
            early_end = False
            for char in word:
                if '#' in node:
                    new_words.append(node['#'])
                    early_end = True
                    break
                if char in node:
                    node = node[char]
                else:
                    new_words.append(word)
                    early_end = True
                    break
            if not early_end:
                if '#' in node:
                    new_words.append(node['#'])
                else:
                    new_words.append(word)
                
        return ' '.join(new_words)