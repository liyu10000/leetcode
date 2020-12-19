# naive stack, O(n*k) time
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if len(stack) >= k-1:
                flag = True
                for i in range(len(stack)-k+1, len(stack)):
                    if stack[i] != c:
                        flag = False
                        break
                if flag:
                    stack = stack[:-(k-1)]
                    continue
            stack.append(c)
        return ''.join(stack)

# stack, record the count
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()                    
            else:
                stack.append([c, 1])
        res = ''
        for c,cnt in stack:
            res += c*cnt
        return res