# first try: time limit exceeded
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        def isTransformation(word1, word2):
            for i in range(len(word1)):
                if word1[:i]+word1[i+1:] == word2[:i]+word2[i+1:]:
                    return True
            return False
        
        queue = [beginWord]
        steps = 1
        while wordList:
            print(steps, queue, wordList)
            steps += 1
            l = len(queue)
            rest = []
            for i in range(l):
                word = queue[i]
                for w in wordList:
                    if isTransformation(word, w):
                        print(word, w)
                        if w == endWord:
                            return steps
                        queue.append(w)
                    else:
                        rest.append(w)
            queue = queue[l:]
            wordList = rest
            
        return 0


# second try
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordMap = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wordMap[word[:i]+'#'+word[i+1:]].append(word)
                
        visited = {word:False for word in wordList}
        
        def getTransformations(word):
            ts = []
            for i in range(len(word)):
                ts += wordMap[word[:i]+'#'+word[i+1:]]
            return ts
        
        queue = [beginWord]
        steps = 1
        while queue:
            steps += 1
            l = len(queue)
            for i in range(l):
                word = queue[i]
                ts = getTransformations(word)
                for w in ts:
                    if w == endWord:
                        return steps
                    if not visited[w]:
                        visited[w] = True
                        queue.append(w)
            queue = queue[l:]
            
        return 0
                             