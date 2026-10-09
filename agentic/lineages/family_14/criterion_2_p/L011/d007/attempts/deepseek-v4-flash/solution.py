import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    anchors = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    degree = [0] * n
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        degree[u] += 1
        degree[v] += 1
        edges.append((u, v, w))
    
    # Leaf pruning
    q = deque()
    removed = [False] * n
    for i in range(n):
        if degree[i] == 1 and i not in anchors:
            q.append(i)
    
    while q:
        u = q.popleft()
        if removed[u]:
            continue
        removed[u] = True
        for v, w in adj[u]:
            if not removed[v]:
                degree[v] -= 1
                if degree[v] == 1 and v not in anchors:
                    q.append(v)
    
    # Sum weights of edges where both endpoints are not removed
    total = 0
    for u, v, w in edges:
        if not removed[u] and not removed[v]:
            total += w
    
    print(total)

if __name__ == "__main__":
    solve()