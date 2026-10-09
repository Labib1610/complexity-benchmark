import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    color = [-1] * n
    camp0 = []
    camp1 = []
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            camp0.append(i)
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            camp0.append(v)
                        else:
                            camp1.append(v)
                        q.append(v)
    
    if len(camp0) >= k:
        ans = camp0[:k]
    elif len(camp1) >= k:
        ans = camp1[:k]
    else:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(x+1) for x in ans))

if __name__ == "__main__":
    solve()