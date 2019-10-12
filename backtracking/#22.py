class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(pre, i, j, res):
            if i + j == 2*n:
                if i == j:
                    res.append(pre)
                return
                    
            if i > j:
                generate(pre+'(', i+1, j, res)
                generate(pre+')', i, j+1, res)
            elif i == j:
                generate(pre+'(', i+1, j, res)
                
        res = []
        generate('', 0, 0, res)
        return res
