from collections import defaultdict, deque
import sys

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    k = int(data[idx])
    idx += 1
    
    products = []
    for _ in range(k):
        s = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        t = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        d = int(data[idx])
        idx += 1
        products.append((s, t, d))
    
    edges = []
    edge_index = {}
    capacity = []
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for i in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        v = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        cap = int(data[idx])
        idx += 1
        edges.append((u, v))
        edge_index[(u, v)] = i
        capacity.append(cap)
        graph[u].append(v)
        reverse_graph[v].append(u)
    
    # Total flow on each edge
    total_flow = [0] * m
    
    # For each product, we need to find a flow
    product_flows = []
    
    # We will solve this by solving k separate max-flow problems
    # But we need to ensure that the sum of flows on each edge does not exceed capacity
    
    # This is a multi-commodity flow problem, which is NP-hard in general.
    # However, we can try to solve it using the following approach:
    # 1. For each commodity, find a flow (ignoring other commodities)
    # 2. Check if the total flow on each edge is within capacity
    # 3. If not, try to adjust flows
    
    # Let's first try a greedy approach:
    # For each commodity, find a path and push flow along it, respecting current total capacity
    
    def bfs_path(graph, source, sink):
        visited = [False] * n
        parent = [-1] * n
        queue = deque()
        queue.append(source)
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        # Reconstruct path
                        path = []
                        current = sink
                        while current != -1:
                            path.append(current)
                            current = parent[current]
                        path.reverse()
                        return path
                    queue.append(v)
        return None
    
    # For each product, we need to send 'd' units from s to t
    # We'll use a simple path decomposition approach
    product_edge_flows = []
    
    for s, t, d in products:
        # Find d paths from s to t (this is a simplification)
        # In reality, we should use a flow decomposition
        # But for simplicity, let's try to find paths and push flow
        
        # Let's build a residual graph that respects current total flow
        # This is getting complex, so let's try a different approach
        
        # Let's use a greedy method:
        # For each unit of flow, find a path and push it
        
        flow_per_edge = [0] * m  # Flow for this product on each edge
        
        for _ in range(d):
            # Build residual graph with current total flows
            res_graph = defaultdict(list)
            for i in range(m):
                u, v = edges[i]
                if total_flow[i] < capacity[i]:
                    res_graph[u].append(v)
            
            # Find a path from s to t
            visited = [False] * n
            parent = [-1] * n
            queue = deque()
            queue.append(s)
            visited[s] = True
            found = False
            
            while queue and not found:
                u = queue.popleft()
                for v in res_graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        parent[v] = u
                        if v == t:
                            found = True
                            break
                        queue.append(v)
            
            if not found:
                print("NO")
                return
                
            # Reconstruct path
            path = []
            current = t
            while current != -1:
                path.append(current)
                current = parent[current]
            path.reverse()
            
            # Push flow along the path
            for i in range(len(path) - 1):
                u = path[i]
                v = path[i+1]
                edge_idx = edge_index[(u, v)]
                flow_per_edge[edge_idx] += 1
                total_flow[edge_idx] += 1
                
                if total_flow[edge_idx] > capacity[edge_idx]:
                    print("NO")
                    return
        
        product_edge_flows.append(flow_per_edge)
    
    print("YES")
    for flow_list in product_edge_flows:
        print(' '.join(map(str, flow_list)))

solve()