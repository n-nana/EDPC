#EDPC_U - Grouping
#Bit DP

N = int(input())

A = []
for _ in range(N):
    a = list(map(int,input().split()))
    A.append(a)

# スコアの前計算
score = [0]*(1<<N)
for st in range(1<<N):
    for i in range(N):
        for j in range(i,N):
            if (st&(1<<i) == 0) or (st&(1<<j) == 0):
                continue
            score[st] += A[i][j]

dp = [0]*(1<<N)
for st in range(1<<N):
    sub = st
    while sub >= 0:
        sub &= st
        dp[st] = max(dp[st], dp[sub] + score[st - sub])
        sub -= 1
    
print(dp[(1<<N)-1])
