class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # serialize operations
        num_stack = []
        op_stack = []
        n = ''
        for c in input:
            if c in '+-*':
                if n:
                    num_stack.append(int(n))
                    n = ''
                op_stack.append(c)
            else:
                n += c
        if n:
            num_stack.append(int(n))
        
        if not op_stack:
            return num_stack
        
        # do calculations
        return self.splitAndCalc(num_stack, op_stack)
    
    def calc(self, n1, op, n2):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        else:
            return n1 * n2
    
    def splitAndCalc(self, num_stack, op_stack):
        if len(num_stack) == 1:
            return num_stack
        else:
            res = []
            for i,op in enumerate(op_stack):
                n1_list = self.splitAndCalc(num_stack[:i+1], op_stack[:i])
                n2_list = self.splitAndCalc(num_stack[i+1:], op_stack[i+1:])
                for n1 in n1_list:
                    for n2 in n2_list:
                        r = self.calc(n1, op, n2)
                        res.append(r)
            return res
                