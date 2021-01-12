class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def helper1(stack, score):
            newstack = []
            for c in stack:
                if newstack and newstack[-1] == 'a' and c == 'b':
                    score += x
                    newstack.pop()
                else:
                    newstack.append(c)
            if len(newstack) < len(stack):
                return helper2(newstack, score)
            return score
                    
        def helper2(stack, score):
            # nonlocal score
            # print(score, stack)
            newstack = []
            for c in stack:
                if newstack and newstack[-1] == 'b' and c == 'a':
                    score += y
                    newstack.pop()
                else:
                    newstack.append(c)
            if len(newstack) < len(stack):
                return helper1(newstack, score)
            return score

        return max(helper1(s, 0), helper2(s, 0))