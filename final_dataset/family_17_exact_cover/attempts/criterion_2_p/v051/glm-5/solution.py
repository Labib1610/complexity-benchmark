import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    # adjacency list: acid -> list of (base, edge_index)
    adj = [[] for _ in range(q + 1)]
    edges = []
    for i in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append((b, i))
        edges.append((a, b))
    
    # Hopcroft-Karp for maximum matching
    pair_acid = [0] * (q + 1)  # 1-indexed acids
    pair_base = {}              # base -> acid
    dist = [0] * (q + 1)
    
    from collections import deque
    
    INF = float('inf')
    
    def bfs():
        queue = deque()
        for a in range(1, q + 1):
            if pair_acid[a] == 0:
                dist[a] = 0
                queue.append(a)
            else:
                dist[a] = INF
        dist[0] = INF
        while queue:
            a = queue.popleft()
            if dist[a] < dist[0]:
                for b, _ in adj[a]:
                    nb = pair_base.get(b, 0)
                    if dist[nb] == INF:
                        dist[nb] = dist[a] + 1
                        queue.append(nb)
        return dist[0] != INF
    
    def dfs(a):
        if a != 0:
            for b, _ in adj[a]:
                nb = pair_base.get(b, 0)
                if dist[nb] == dist[a] + 1 and dfs(nb):
                    pair_base[b] = a
                    pair_acid[a] = b
                    return True
            dist[a] = INF
            return False
        return True
    
    matching = 0
    while bfs():
        for a in range(1, q + 1):
            if pair_acid[a] == 0:
                if dfs(a):
                    matching += 1
    
    if matching != q:
        sys.stdout.write("NO\n")
        return
    
    # Build edge index lookup: (acid, base) -> edge_index
    edge_index = {}
    for i, (a, b) in enumerate(edges):
        edge_index[(a, b)] = i
    
    # Find selected edges
    selected = []
    for a in range(1, q + 1):
        b = pair_acid[a]
        idx = edge_index[(a, b)]
        selected.append(idx)
    
    out = ["YES"]
    for idx in selected:
        a, b = edges[idx]
        out.append(f"{a} {b}")
    sys.stdout.write("\n".join(out) + "\n")

solve()