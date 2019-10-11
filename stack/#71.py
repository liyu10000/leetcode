class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for p in path:
            if p == '.' or p == '':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        res = '/' + '/'.join(stack)
        return res