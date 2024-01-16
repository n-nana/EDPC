# S - Digit Sum (https://atcoder.jp/contests/dp/tasks/dp_s)
# 桁DP

# https://kyopro-friends.hatenablog.com/entry/2019/01/12/231035
# https://blog.hamayanhamayan.com/entry/2019/01/12/144102

#---------------------------------------------------------------
MOD = 10**9 + 7

K = list(input())
D = int(input())
N = len(K)

dp = [[[0]*D for i in range(N+1)] for s in range(2)] # rem, dig, state
dp[1][0][0] = 1

for i in range(N): # digit
    for j in range(D): # rem
        for s in range(2): # flag
            for d in range(10):
                ni = i + 1
                nj = (j + d)%D
                if s == 1: # 判定あり
                    if d > int(K[i]):
                        continue
                    if d == int(K[i]):
                        dp[s][ni][nj] += dp[s][i][j]
                        dp[s][ni][nj] %= MOD
                    if d < int(K[i]):
                        dp[0][ni][nj] += dp[s][i][j]
                        dp[0][ni][nj] %= MOD
                else: # 判定なし
                    dp[s][ni][nj] += dp[s][i][j]
                    dp[s][ni][nj] %= MOD

ans = (dp[0][N][0] + dp[1][N][0] - 1)%MOD
print(max(ans, 0))
