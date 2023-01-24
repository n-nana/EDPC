#ABC286D - Money in Hand
#個数制限付き部分和, 個数制約付きナップサック
#計算量NX ver.

INF = 60
N,X = map(int,input().split())

dp = [[INF]*(X+3) for _ in range(N+3)]
dp[0][0] = 0

for i in range(N):
    A,B = map(int,input().split())
    for j in range(X+1):
        #硬貨A[i]を使わない場合、
        if dp[i][j] != INF: 
            dp[i+1][j] = dp[i][j]
        #硬貨A[i]を使う場合、
        if A <= j:
            pre = j - A
            #硬貨Aを1枚使う場合、
            if dp[i][pre] != INF: 
                dp[i+1][j] = min(1, dp[i+1][j])
            #硬貨AをB枚まで使う場合、
            if dp[i+1][pre] < B:
                dp[i+1][j] = min(dp[i+1][pre]+1, dp[i+1][j])

if dp[N][X] != INF: print("Yes")
else: print("No")
    
#print(*dp, sep="\n")
