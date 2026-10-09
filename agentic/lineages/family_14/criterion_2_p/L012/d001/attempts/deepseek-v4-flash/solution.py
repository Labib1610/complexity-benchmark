import sys
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.buffer.read().split()
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    primary = set()
    idx = 3
    for _ in range(t):
        primary.add(int(input_data[idx]))
        idx += 1
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        w = int(input_data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    degree = [len(adj[i]) for i in range(n + 1)]
    visited = [False] * (n + 1)
    
    # Queue of leaves that are not primary hubs
    from collections import deque
    q = deque()
    for i in range(1, n + 1):
        if degree[i] == 1 and i not in primary:
            q.append(i)
    
    removed = [False] * (n + 1)
    while q:
        u = q.popleft()
        removed[u] = True
        for v, w in adj[u]:
            if not removed[v]:
                degree[v] -= 1
                if degree[v] == 1 and v not in primary:
                    q.append(v)
    
    total = 0
    for u, v, w in edges:
        if not removed[u] and not removed[v]:
            total += w
    
    print(total)

if __name__ == "__main__":
    solve()