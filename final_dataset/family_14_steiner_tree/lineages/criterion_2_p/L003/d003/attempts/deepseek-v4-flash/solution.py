import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    degree = [len(adj[i]) for i in range(n + 1)]
    visited = [False] * (n + 1)
    q = deque()
    
    for i in range(1, n + 1):
        if degree[i] == 1 and i not in critical:
            q.append(i)
            visited[i] = True
    
    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                degree[v] -= 1
                if degree[v] == 1 and v not in critical:
                    visited[v] = True
                    q.append(v)
    
    total_cost = 0
    for u, v, w in edges:
        if not visited[u] and not visited[v]:
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    solve()