import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    hubs = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    edge_cost = {}
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        degree[u] += 1
        degree[v] += 1
        edge_cost[(u, v)] = w
        edge_cost[(v, u)] = w
    
    # If only one hub, cost is 0
    if t == 1:
        print(0)
        return
    
    # Remove non-hub leaves
    q = deque()
    removed = [False] * (n + 1)
    for i in range(1, n + 1):
        if degree[i] == 1 and i not in hubs:
            q.append(i)
    
    total_cost = 0
    while q:
        u = q.popleft()
        if removed[u]:
            continue
        removed[u] = True
        for v, w in adj[u]:
            if not removed[v]:
                total_cost += w
                degree[v] -= 1
                if degree[v] == 1 and v not in hubs:
                    q.append(v)
    
    print(total_cost)

if __name__ == "__main__":
    solve()