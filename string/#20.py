class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in m:
                if stack and stack[-1] == m[c]:
                    _ = stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
            