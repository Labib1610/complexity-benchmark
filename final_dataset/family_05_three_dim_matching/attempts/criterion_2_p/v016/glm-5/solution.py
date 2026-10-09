import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    edges = []
    for _ in range(t):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    # Bipartite matching between transmitters (left) and carrier frequencies (right)
    # Left side: 1..k, Right side: k+1..2k
    N = 2 * k + 2
    source = 0
    sink = 2 * k + 1
    
    capacity = [[0] * N for _ in range(N)]
    graph = [[] for _ in range(N)]
    
    # Build graph
    for u, v, w in edges:
        # u is transmitter, w is frequency
        cap = 1
        capacity[u][k + w] += cap
        graph[u].append(k + w)
        graph[k + w].append(u)
    
    for u in range(1, k + 1):
        capacity[source][u] = 1
        graph[source].append(u)
        graph[u].append(source)
    
    for w in range(1, k + 1):
        capacity[k + w][sink] = 1
        graph[k + w].append(sink)
        graph[sink].append(k + w)
    
    # Dinic's algorithm
    level = [0] * N
    ptr = [0] * N
    
    def bfs():
        for i in range(N):
            level[i] = -1
        level[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if level[v] == -1 and capacity[u][v] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[sink] != -1
    
    def dfs(u, flow):
        if u == sink:
            return flow
        for i in range(ptr[u], len(graph[u])):
            v = graph[u][i]
            if level[v] == level[u] + 1 and capacity[u][v] > 0:
                pushed = dfs(v, min(flow, capacity[u][v]))
                if pushed > 0:
                    capacity[u][v] -= pushed
                    capacity[v][u] += pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    def max_flow():
        total_flow = 0
        while bfs():
            ptr = [0] * N
            while True:
                flow = dfs(source, float('inf'))
                if flow == 0:
                    break
                total_flow += flow
        return total_flow
    
    flow = max_flow()
    
    if flow < k:
        print("NO")
        return
    
    # Reconstruct matching
    match = {}  # u -> w
    for u in range(1, k + 1):
        for w in range(1, k + 1):
            if capacity[k + w][u] > 0:  # reverse edge has flow
                match[u] = w
                break
    
    # Build result
    # We need to output u v w for each transmitter u
    # v is determined by the hardwiring constraint
    # We need to find which v corresponds to transmitter u
    # From the problem statement: each transmitter is hardwired to exactly one cryptographic module
    # So for each u, all edges involving u have the same v
    
    # First, find the v for each transmitter
    tx_to_crypto = {}
    for u, v, w in edges:
        if u not in tx_to_crypto:
            tx_to_crypto[u] = v
        # else: should be same v, guaranteed by problem
    
    result = []
    for u in range(1, k + 1):
        if u in match:
            w = match[u]
            v = tx_to_crypto[u]
            result.append((u, v, w))
    
    print("YES")
    for u, v, w in result:
        print(u, v, w)

if __name__ == "__main__":
    solve()