import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    is_terminal = [False] * (n + 1)
    for i in range(t):
        v = int(input_data[idx]); idx += 1
        is_terminal[v] = True
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, i))
        adj[v].append((u, i))
        edges.append(w)
    
    if t <= 1:
        print(0)
        return
    
    degree = [0] * (n + 1)
    for u in range(1, n + 1):
        degree[u] = len(adj[u])
    
    removed = [False] * (n + 1)
    edge_removed = [False] * m
    queue = deque()
    
    for v in range(1, n + 1):
        if degree[v] == 1 and not is_terminal[v]:
            queue.append(v)
    
    while queue:
        v = queue.popleft()
        if removed[v] or degree[v] != 1:
            continue
        removed[v] = True
        for (neighbor, edge_idx) in adj[v]:
            if not edge_removed[edge_idx]:
                edge_removed[edge_idx] = True
                degree[neighbor] -= 1
                degree[v] -= 1
                if degree[neighbor] == 1 and not is_terminal[neighbor] and not removed[neighbor]:
                    queue.append(neighbor)
                break
    
    total = 0
    for i in range(m):
        if not edge_removed[i]:
            total += edges[i]
    
    print(total)

solve()