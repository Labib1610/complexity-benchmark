import sys
from collections import deque

def max_flow(n, graph, s, t):
    flow = 0
    while True:
        parent = [-1]*n
        parent[s] = s
        q = deque([s])
        while q and parent[t] == -1:
            u = q.popleft()
            for v, cap in graph[u].items():
                if parent[v] == -1 and cap > 0:
                    parent[v] = u
                    q.append(v)
        if parent[t] == -1:
            break
        # find bottleneck
        v = t
        aug = float('inf')
        while v != s:
            u = parent[v]
            aug = min(aug, graph[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= aug
            graph[v][u] = graph.get(v, {}).get(u, 0) + aug
            v = u
        flow += aug
    return flow

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    commodities = []
    for _ in range(k):
        s = int(next(it))-1
        t = int(next(it))-1
        d = int(next(it))
        commodities.append((s,t,d))
    edges = []
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        cap = int(next(it))
        edges.append((u,v,cap))
    
    # We'll try to route each commodity sequentially, updating capacities
    caps = [e[2] for e in edges]
    flows = [[0]*m for _ in range(k)]
    
    for idx, (s,t,d) in enumerate(commodities):
        # Build graph with current capacities
        graph = [{} for _ in range(n)]
        for j,(u,v,cap) in enumerate(edges):
            graph[u][v] = caps[j]
            graph[v][u] = 0  # reverse edge for residual
        # We need to send d units from s to t
        # Use max flow but we need exactly d, not max
        # We'll do repeated augmenting until d is sent
        sent = 0
        while sent < d:
            parent = [-1]*n
            parent[s] = s
            q = deque([s])
            while q and parent[t] == -1:
                u = q.popleft()
                for v, cap in graph[u].items():
                    if parent[v] == -1 and cap > 0:
                        parent[v] = u
                        q.append(v)
            if parent[t] == -1:
                print("NO")
                return
            # find bottleneck
            v = t
            aug = float('inf')
            path_edges = []
            while v != s:
                u = parent[v]
                aug = min(aug, graph[u][v])
                # find edge index
                for j,(eu,ev,cap) in enumerate(edges):
                    if eu == u and ev == v:
                        path_edges.append(j)
                        break
                v = u
            # limit to remaining demand
            aug = min(aug, d - sent)
            v = t
            while v != s:
                u = parent[v]
                graph[u][v] -= aug
                graph[v][u] = graph.get(v, {}).get(u, 0) + aug
                v = u
            sent += aug
            for j in path_edges:
                flows[idx][j] += aug
                caps[j] -= aug
        # after sending, update caps for next commodity
    print("YES")
    for row in flows:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()