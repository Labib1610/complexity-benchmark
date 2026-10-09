import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    cores = []
    for _ in range(t):
        cores.append(int(input_data[idx]) - 1)
        idx += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    root = cores[0]
    
    parent = [(-1, 0)] * n
    visited = [False] * n
    visited[root] = True
    stack = [root]
    
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = (u, w)
                stack.append(v)
    
    marked = [False] * n
    total = 0
    
    for c in cores:
        node = c
        while node != root:
            p, w = parent[node]
            if marked[node]:
                break
            marked[node] = True
            total += w
            node = p
    
    print(total)

solve()