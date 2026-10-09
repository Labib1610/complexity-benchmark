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
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
    
    group0 = [i+1 for i in range(n) if color[i] == 0]
    group1 = [i+1 for i in range(n) if color[i] == 1]
    
    if len(group0) >= k:
        print("YES")
        print(" ".join(map(str, group0[:k])))
    elif len(group1) >= k:
        print("YES")
        print(" ".join(map(str, group1[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()