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


# build a 2d table first and do BFS, get TLE
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # build a 2d table recording connectivity of each word pairs
        if beginWord in wordList:
            fullWordList = wordList
            i = wordList.index(beginWord)
        else:
            fullWordList = [beginWord] + wordList
            i = 0
        j = fullWordList.index(endWord)
        n = len(fullWordList)
        t = [[0] * n for _ in range(n)]
        for u in range(n):
            for v in range(u+1, n):
                t[u][v] = t[v][u] = self.oneLetterDiff(fullWordList[u], fullWordList[v])
        
        # BFS search for shortest path
        steps = 1
        visited = {i} # record indices
        queue = [i]  # queue of indices
        while queue:
            steps += 1
            newqueue = []
            for u in queue:
                for v in range(n):
                    if t[u][v]:
                        if v == j:
                            return steps
                        if not v in visited:
                            visited.add(v)
                            newqueue.append(v)
            queue = newqueue
        
        return 0
    
    
    def oneLetterDiff(self, word1, word2):
        diff = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff += 1
                if diff > 1:
                    return 0
        return diff
