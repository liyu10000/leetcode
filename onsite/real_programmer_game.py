from pprint import pprint

# backtrack get TLE or even OOM
def backtrack(n, m, k, s, count):
    # print(k, s, count)
    if k == 0:
        if s >= n:
            count[0] += 1
        count[1] += 1
        return 
    if s >= n:
        remain = (m + 1) ** k
        count[0] += remain
        count[1] += remain
        return
    for i in range(m+1):
        backtrack(n, m, k-1, s+i, count)

def rpg(n, m, k):
    count = [0, 0]  # right, total
    backtrack(n, m, k, 0, count)
    print(count)
    return round(count[0] / count[1], 6)

def rpg(n, m, k):
    if n > m * k:
        return 0.0
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == 1:
                dp[i][j] = j
            elif i == 2:
                dp[i][j] = j * j
            else:
                if j == 1:
                    dp[i][j] = 1
                elif j == 2:
                    dp[i][j] = n * (n - 1) // 2
                else:
                    for u in range(1, i):
                        for v in range(1, j):
                            dp[i][j] += dp[u][v] * dp[i-u][j-v]
    pprint(dp)
    # p = dp[n][k] / 


def factorial(n):
    if n == 1:
       return n
    else:
       return n*factorial(n-1)



if __name__ == '__main__':
    n = 5
    m = 2
    k = 3
    p = rpg(n, m, k)
    print(p)
    
    print(factorial(5))
