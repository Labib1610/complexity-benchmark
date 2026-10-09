import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    signatures = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        signatures.append((s, t, d))
    
    edges_input = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges_input.append((u, v, cap))
    
    # Build graph for multi-commodity flow
    # Node indexing: 0..n-1 are original nodes
    # We'll use adjacency list with edge objects
    
    class Edge:
        __slots__ = ('to', 'cap', 'flow', 'rev', 'commodity')
        def __init__(self, to, cap, rev, commodity=-1):
            self.to = to
            self.cap = cap
            self.flow = 0
            self.rev = rev
            self.commodity = commodity  # -1 for shared capacity edges
    
    graph = [[] for _ in range(n)]
    edge_indices = []  # To track which input edge corresponds to which graph edge
    
    for u, v, cap in edges_input:
        u -= 1
        v -= 1
        idx_u = len(graph[u])
        idx_v = len(graph[v])
        graph[u].append(Edge(v, cap, idx_v, -1))
        graph[v].append(Edge(u, 0, idx_u, -1))
        edge_indices.append((u, idx_u))
    
    # For each commodity, we need to find flow from s_i to t_i with demand d_i
    # We'll use successive shortest augmenting path (Edmonds-Karp style)
    
    def bfs(source, sink, parent_edge):
        """Find augmenting path using BFS"""
        for i in range(n):
            parent_edge[i] = -1
        queue = deque([source])
        parent_edge[source] = -2  # Mark as visited
        
        while queue:
            u = queue.popleft()
            for e in graph[u]:
                if e.commodity != -1:
                    continue  # Skip commodity-specific edges for now
                if e.cap > e.flow and parent_edge[e.to] == -1:
                    parent_edge[e.to] = e
                    if e.to == sink:
                        return True
                    queue.append(e.to)
        return False
    
    def max_flow(source, sink, max_amount):
        """Find max flow up to max_amount"""
        flow = 0
        parent_edge = [-1] * n
        
        while flow < max_amount and bfs(source, sink, parent_edge):
            # Find bottleneck
            path_flow = max_amount - flow
            v = sink
            while v != source:
                e = parent_edge[v]
                path_flow = min(path_flow, e.cap - e.flow)
                v = graph[e.to][e.rev].to  # Go back through reverse edge
            
            # Augment path
            v = sink
            while v != source:
                e = parent_edge[v]
                e.flow += path_flow
                graph[e.to][e.rev].flow -= path_flow
                v = graph[e.to][e.rev].to
            
            flow += path_flow
        
        return flow
    
    # Process each commodity
    result = [[0] * m for _ in range(k)]
    
    for i, (s, t, d) in enumerate(signatures):
        s -= 1
        t -= 1
        flow = max_flow(s, t, d)
        if flow < d:
            print("NO")
            return
        
        # Record flow on each edge for this commodity
        for j, (u, idx) in enumerate(edge_indices):
            e = graph[u][idx]
            result[i][j] = e.flow
        
        # Reset flows for next commodity (but keep track of total usage)
        # Actually, we need to keep the flow for capacity constraints
        # The flow on shared edges accumulates
    
    # Verify total flow on each edge doesn't exceed capacity
    for j, (u, idx) in enumerate(edge_indices):
        e = graph[u][idx]
        total = sum(result[comp][j] for comp in range(k))
        if total > edges_input[j][2]:
            print("NO")
            return
    
    print("YES")
    for row in result:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    solve()