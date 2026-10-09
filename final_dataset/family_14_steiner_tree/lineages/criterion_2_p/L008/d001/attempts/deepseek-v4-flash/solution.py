import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    high = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        deg[u] += 1
        deg[v] += 1
        edges.append((u, v, w))
    
    removed = [False] * (n + 1)
    q = deque()
    
    for i in range(1, n + 1):
        if deg[i] == 1 and i not in high:
            q.append(i)
    
    while q:
        u = q.popleft()
        if removed[u]:
            continue
        removed[u] = True
        for v, w in adj[u]:
            if not removed[v]:
                deg[v] -= 1
                if deg[v] == 1 and v not in high:
                    q.append(v)
    
    total = 0
    for u, v, w in edges:
        if not removed[u] and not removed[v]:
            total += w
    
    print(total)

if __name__ == "__main__":
    solve()