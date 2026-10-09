import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    
    try:
        n = int(next(it))
        m = int(next(it))
        _ = int(next(it))  # constant 1
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
    except StopIteration:
        return
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append(v)
    
    # Build capacity graph for Dinic's algorithm
    capacity = [[0] * (n + 1) for _ in range(n + 1)]
    edge_to_idx = {}
    for i, (u, v, cap) in enumerate(edges):
        capacity[u][v] += cap
        if (u, v) in edge_to_idx:
            # Multiple edges between same nodes, sum capacities
            pass
        edge_to_idx[(u, v)] = i
    
    # Dinic's algorithm
    level = [0] * (n + 1)
    
    def bfs():
        nonlocal level
        level = [0] * (n + 1)
        queue = [s]
        level[s] = 1
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v in range(1, n + 1):
                if capacity[u][v] > 0 and level[v] == 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level[t] != 0
    
    def dfs(u, flow):
        if u == t:
            return flow
        total_pushed = 0
        for v in range(1, n + 1):
            if capacity[u][v] > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(flow - total_pushed, capacity[u][v]))
                if pushed > 0:
                    capacity[u][v] -= pushed
                    capacity[v][u] += pushed
                    total_pushed += pushed
                    if total_pushed == flow:
                        break
        return total_pushed
    
    max_flow = 0
    while bfs():
        max_flow += dfs(s, d - max_flow)
        if max_flow >= d:
            break
    
    if max_flow < d:
        print("NO")
        return
    
    print("YES")
    
    # Extract flow values for each edge
    result = [0] * m
    for i, (u, v, cap) in enumerate(edges):
        flow_on_edge = cap - capacity[u][v]
        capacity[u][v] = cap  # Restore original capacity for next calculation
        result[i] = flow_on_edge
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()