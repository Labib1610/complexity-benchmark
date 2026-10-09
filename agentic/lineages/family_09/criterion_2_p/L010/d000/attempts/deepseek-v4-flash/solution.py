import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    group0 = []
    group1 = []
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            group0.append(i)
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            group0.append(v)
                        else:
                            group1.append(v)
                        q.append(v)
    
    if len(group0) >= k:
        chosen = group0[:k]
    elif len(group1) >= k:
        chosen = group1[:k]
    else:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(x + 1) for x in chosen))

if __name__ == "__main__":
    solve()