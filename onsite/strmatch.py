"""
Problem: match two strings. Each string could contain characters a-z, A-Z, and 0-9. If a number exists in the string, it means that the string contains a number of unknown characters, which can be matched with any characters of the same length.
Example:
    1. "A2Le" == "2pL1"
    2. "a10" == "10a"
    3. "3x2x" != "8"

Write a function:
    def sulution(S, T):
        pass
"""


def getNum(s, i, n):
    num = 0
    while i < n and 48 <= ord(s[i]) <= 57:
        num = num * 10 + (ord(s[i]) - 48)
        i += 1
    return num, i
    
def refill(s):
    res = ''
    i = 0
    while i < len(s):
        if 48 <= ord(s[i]) <= 57:
            num, i = getNum(s, i, len(s))
            res += '.' * num
        else:
            res += s[i]
            i += 1
    return res
        

def solution(S, T):
    # write your code in Python 3.6
    S_refilled = refill(S)
    T_refilled = refill(T)
    
    if len(S_refilled) != len(T_refilled):
        return False
        
    for s, t in zip(S_refilled, T_refilled):
        if s != '.' and t != '.' and s != t:
            return False
    return True
    

# this solution is better
def solution(S, T):
    # write your code in Python 3.6
    N, M = len(S), len(T)
    i, j = 0, 0
    Spad, Tpad = '', ''
    while True:
        if i == N and j == M:
            break

        if i < N:
            if 48 <= ord(S[i]) <= 57:
                num, i = getNum(S, i, N)
                Spad += '.' * num
            else:
                Spad += S[i]
                i += 1

        if j < M:
            if 48 <= ord(T[j]) <= 57:
                num, j = getNum(T, j, M)
                Tpad += '.' * num
            else:
                Tpad += T[j]
                j += 1

        padi = 0
        while padi < len(Spad) and padi < len(Tpad):
            if Spad[padi] != '.' and Tpad[padi] != '.' and Spad[padi] != Tpad[padi]:
                return False
            padi += 1
        Spad = Spad[padi:]
        Tpad = Tpad[padi:]

    return Spad == Tpad


if __name__ == '__main__':
    S = 'a100000b'
    S_refilled = refill(S)
    # print(S_refilled)

    T = '100000aa'
    T_refilled = refill(T)
    # print(T_refilled)

    print(solution(S, T))