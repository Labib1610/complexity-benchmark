import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    q = int(next(iterator))
    t = int(next(iterator))
    
    # Nodes 1..q are extractors, nodes q+1..2q are vents
    n_total = 2 * q + 2  # including source 0 and sink 2q+1
    source = 0
    sink = 2 * q + 1
    
    # Build adjacency list for Dinic's algorithm
    # Each entry: (to, capacity, rev_index)
    adj = [[] for _ in range(n_total)]
    edges = []  # Store original edges to output later
    
    def add_edge(u, v, cap):
        adj[u].append([v, cap, len(adj[v])])
        adj[v].append([u, 0, len(adj[u]) - 1])
    
    # Source to extractors
    for i in range(1, q + 1):
        add_edge(source, i, 1)
    
    # Vents to sink
    for i in range(q + 1, 2 * q + 1):
        add_edge(i, sink, 1)
    
    # Intact pipes
    for _ in range(t):
        a = int(next(iterator))
        b = int(next(iterator))
        edges.append((a, b))
        add_edge(a, b, 1)
    
    # Dinic's algorithm
    level = [0] * n_total
    ptr = [0] * n_total
    
    def bfs():
        for i in range(n_total):
            level[i] = -1
        level[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v, cap, rev in adj[u]:
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level[sink] != -1
    
    def dfs(u, flow):
        if u == sink:
            return flow
        while ptr[u] < len(adj[u]):
            v, cap, rev = adj[u][ptr[u]]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(flow, cap))
                if pushed > 0:
                    adj[u][ptr[u]][1] -= pushed
                    adj[v][rev][1] += pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    max_flow = 0
    while bfs():
        ptr = [0] * n_total
        while True:
            pushed = dfs(source, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed
    
    if max_flow != q:
        print("NO")
        return
    
    print("YES")
    # Find the matching
    for a, b in edges:
        # Check if edge a->b is used (capacity 0 means used)
        for v, cap, rev in adj[a]:
            if v == b and cap == 0:
                print(a, b)
                break

if __name__ == "__main__":
    solve()