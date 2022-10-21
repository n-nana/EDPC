import sys
sys.setrecursionlimit(10**7)

def rec(crr):
    done[crr] = True
    
    for nxt in G[crr]:
        if done[nxt]:
            res[crr] = max(res[nxt]+1, res[crr])
            continue
        rec(nxt)
        res[crr] = max(res[nxt]+1, res[crr])

N,M = map(int,input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    x,y = map(int,input().split())
    G[x-1].append(y-1)

done = [False]*N
res = [0]*N
for i in range(N):
    if done[i]: continue
    rec(i)
    
print(max(res))
