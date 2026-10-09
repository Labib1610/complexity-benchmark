import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    tier0 = []
    tier1 = []
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            tier0.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            tier0.append(v)
                        else:
                            tier1.append(v)
                        q.append(v)
    
    if len(tier0) >= k:
        print("YES")
        print(" ".join(str(x+1) for x in tier0[:k]))
    elif len(tier1) >= k:
        print("YES")
        print(" ".join(str(x+1) for x in tier1[:k]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()