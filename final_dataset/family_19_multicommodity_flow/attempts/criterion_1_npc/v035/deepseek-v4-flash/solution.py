import sys
from collections import deque

def dinic(n, graph, source, sink):
    # graph: list of edges [to, rev, cap]
    # returns max flow and updates flow
    pass

def main():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    products = []
    for _ in range(k):
        s, t, d = map(int, input().split())
        products.append((s-1, t-1, d))
    lanes = []
    for i in range(m):
        u, v, cap = map(int, input().split())
        lanes.append((u-1, v-1, cap))
    
    # Build max flow graph
    N = n + 2
    S = n
    T = n + 1
    graph = [[] for _ in range(N)]
    
    # Add super source edges
    for i, (s, t, d) in enumerate(products):
        add_edge(graph, S, s, d)
        add_edge(graph, t, T, d)
    
    # Add lane edges
    lane_edge_index = []  # to map to original lane index
    for u, v, cap in lanes:
        # We'll store the forward edge index in graph[u] after adding
        idx = len(graph[u])
        add_edge(graph, u, v, cap)
        lane_edge_index.append((u, idx))
    
    # Run max flow
    flow, _ = max_flow(graph, S, T)
    total_demand = sum(d for _,_,d in products)
    if flow < total_demand:
        print("NO")
        return
    
    # Now decompose per product
    # We need to know flow on each lane
    # We'll store flow per product per lane
    product_flow = [[0]*m for _ in range(k)]
    
    # We'll work with a copy of flow on lanes
    # We can get flow from graph edges
    # For each lane, the forward edge is at graph[u][idx] where idx is stored.
    # We'll create a list lane_flow = []
    lane_flow = []
    for u, idx in lane_edge_index:
        edge = graph[u][idx]
        lane_flow.append(edge['flow'])  # flow on forward edge
    
    # For each product, decompose
    for pi, (s, t, d) in enumerate(products):
        remaining = d
        while remaining > 0:
            # Find a path from s to t using edges with flow > 0
            # We'll do DFS/BFS
            parent = [-1]*n
            parent_edge = [-1]*n
            stack = [s]
            parent[s] = s
            found = False
            while stack:
                u = stack.pop()
                if u == t:
                    found = True
                    break
                # Iterate over original lanes from u
                for ei, (u2, v, cap) in enumerate(lanes):
                    if u2 != u:
                        continue
                    if lane_flow[ei] > 0 and parent[v] == -1:
                        parent[v] = u
                        parent_edge[v] = ei
                        stack.append(v)
            if not found:
                # Should not happen
                print("NO")
                return
            # Find bottleneck
            f = remaining
            v = t
            while v != s:
                ei = parent_edge[v]
                f = min(f, lane_flow[ei])
                v = parent[v]  # actually parent[v] is u
            # Update
            v = t
            while v != s:
                ei = parent_edge[v]
                lane_flow[ei] -= f
                product_flow[pi][ei] += f
                v = parent[v]
            remaining -= f
    
    # Output
    print("YES")
    for i in range(k):
        print(' '.join(str(product_flow[i][j]) for j in range(m)))

if __name__ == "__main__":
    main()