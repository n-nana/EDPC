s = input()
t = input()

N = len(s)
M = len(t)

#LCS
dp = [[0]*(M+3) for _ in range(N+3)]
for i in range(N):
    for j in range(M):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

#経路復元
res = []
i,j = N,M
while i > 0 and j > 0:
    if s[i-1] == t[j-1]: #sとtが一致したら答えに追加して両indexを減らす
        res.append(s[i-1])
        i -= 1
        j -= 1
    else:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1

res.reverse()
print("".join(res))
        
        
    
        
