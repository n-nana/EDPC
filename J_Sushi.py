# EDPC_J - Sushi

#from collections import Counter
#C = Counter(A)

N = int(input())
A = list(map(int,input().split()))
P1 = A.count(1)
P2 = A.count(2)
P3 = A.count(3)

mx = 300
dp = [[[0]*(mx+1) for _ in range(mx+1)] for _ in range(mx+1)]

# dp[i][j][k] = ((N-i-j-k)/N)*dp[i][j][k] + (i/N)*dp[i-1][j][k] + (j/N)*dp[i+1][j-1][k] + (k/N)*dp[i][j+1][k-1] + 1　より
# dp[i][j][k] = (N + i*dp[i-1][j][k] + j*dp[i+1][j-1][k] + k*dp[i][j+1][k-1])/(i+j+k) となる

# 皿を更新する順番に注意
for k in range(N+1): #3個
    for j in range(N+1): #2個
        for i in range(N+1): #1個
            M = i+j+k
            if M == 0:
                continue
            if M > N: # break入れないとTLE and RE
                break
                
            dp[i][j][k] = N #0個の皿を選ぶ場合
            if i > 0:
                dp[i][j][k] += i*(dp[i-1][j][k]) #1個の皿を選ぶ場合
            if j > 0:
                dp[i][j][k] += j*(dp[i+1][j-1][k]) #2個の皿を選ぶ場合               
            if k > 0:
                dp[i][j][k] += k*(dp[i][j+1][k-1]) #3個の皿を選ぶ場合
            
            dp[i][j][k] /= M
            
print(dp[P1][P2][P3])
