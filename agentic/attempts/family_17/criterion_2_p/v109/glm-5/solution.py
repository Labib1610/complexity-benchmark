import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    # Drones: 1 to q, Bays: q+1 to 2q
    # We'll use 0-indexed internally for convenience in some parts, but let's stick to 1-indexed for nodes
    # Total nodes: 2q + 2 (including source and sink)
    # Source = 0, Sink = 2q + 1
    # Drones: 1..q, Bays: q+1..2q
    
    N = 2 * q + 2
    source = 0
    sink = 2 * q + 1
    
    adj = [[] for _ in range(N)]
    capacity = [[0] * N for _ in range(N)]
    
    def add_edge(u, v, cap):
        adj[u].append(v)
        adj[v].append(u)
        capacity[u][v] = cap
    
    # Source to drones
    for i in range(1, q + 1):
        add_edge(source, i, 1)
    
    # Bays to sink
    for i in range(q + 1, 2 * q + 1):
        add_edge(i, sink, 1)
    
    # Drone to Bay edges
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        add_edge(a, b, 1)
    
    # Dinic's algorithm
    level = [0] * N
    ptr = [0] * N
    
    def bfs():
        for i in range(N):
            level[i] = -1
        queue = deque([source])
        level[source] = 0
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if level[v] == -1 and capacity[u][v] > 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level[sink] != -1
    
    def dfs(u, flow):
        if u == sink:
            return flow
        for i in range(ptr[u], len(adj[u])):
            v = adj[u][i]
            if level[v] == level[u] + 1 and capacity[u][v] > 0:
                pushed = dfs(v, min(flow, capacity[u][v]))
                if pushed > 0:
                    capacity[u][v] -= pushed
                    capacity[v][u] += pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    max_flow = 0
    while bfs():
        ptr = [0] * N
        while True:
            pushed = dfs(source, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed
    
    if max_flow == q:
        sys.stdout.write("YES\n")
        # Find assignments
        for u in range(1, q + 1):
            for v in adj[u]:
                if q + 1 <= v <= 2 * q and capacity[u][v] == 0:
                    sys.stdout.write(f"{u} {v}\n")
                    break
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()