import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    edge_weight = {}
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        degree[u] += 1
        degree[v] += 1
        edge_weight[(u, v)] = w
        edge_weight[(v, u)] = w
    
    # Prune non-critical leaves
    q = deque()
    removed = [False] * (n + 1)
    for i in range(1, n + 1):
        if degree[i] == 1 and i not in critical:
            q.append(i)
    
    while q:
        u = q.popleft()
        removed[u] = True
        for v, w in adj[u]:
            if not removed[v]:
                degree[v] -= 1
                if degree[v] == 1 and v not in critical:
                    q.append(v)
    
    total_cost = 0
    for (u, v), w in edge_weight.items():
        if u < v and not removed[u] and not removed[v]:
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    solve()