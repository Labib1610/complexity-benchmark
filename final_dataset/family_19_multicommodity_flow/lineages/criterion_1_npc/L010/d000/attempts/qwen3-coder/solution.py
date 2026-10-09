from collections import defaultdict, deque
import sys

def solve():
    n, m, k = map(int, input().split())
    
    streams = []
    for i in range(k):
        s, t, d = map(int, input().split())
        streams.append((s, t, d))
    
    edges = []
    edge_info = []
    capacity = []
    edge_map = {}
    
    graph = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v))
        edge_info.append((u, v, cap))
        capacity.append(cap)
        edge_map[(u, v)] = i
        graph[u].append((v, i))
    
    # Build aggregated flow network to check feasibility
    # Nodes: 0 (source) + 1..n (switches) + n+1 (sink)
    # Edges: source -> ingress nodes, egress nodes -> sink, original edges
    
    INF = float('inf')
    
    def bfs(cap_graph, source, sink, parent):
        visited = [False] * (n + 2)
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            
            for v, edge_idx, cap, rev_idx in cap_graph[u]:
                if not visited[v] and cap > 0:
                    visited[v] = True
                    parent[v] = (u, edge_idx)
                    if v == sink:
                        return True
                    queue.append(v)
        
        return False
    
    def ford_fulkerson(cap_graph, source, sink):
        parent = [-1] * (n + 2)
        max_flow = 0
        
        while bfs(cap_graph, source, sink, parent):
            path_flow = INF
            s = sink
            
            # Find minimum capacity in the path
            while s != source:
                u, edge_idx = parent[s]
                # Find the actual edge in adjacency list
                for v_node, e_idx, cap, rev_idx in cap_graph[u]:
                    if v_node == s and e_idx == edge_idx:
                        path_flow = min(path_flow, cap)
                        break
                s = u
            
            # Update capacities
            v = sink
            while v != source:
                u, edge_idx = parent[v]
                # Update forward edge
                for i in range(len(cap_graph[u])):
                    if cap_graph[u][i][0] == v and cap_graph[u][i][1] == edge_idx:
                        cap_graph[u][i] = (cap_graph[u][i][0], cap_graph[u][i][1], cap_graph[u][i][2] - path_flow, cap_graph[u][i][3])
                        rev_u, rev_v = cap_graph[u][i][0], u
                        rev_edge_idx = cap_graph[u][i][3]
                        # Update reverse edge
                        for j in range(len(cap_graph[rev_v])):
                            if cap_graph[rev_v][j][0] == rev_u and cap_graph[rev_v][j][1] == rev_edge_idx:
                                cap_graph[rev_v][j] = (cap_graph[rev_v][j][0], cap_graph[rev_v][j][1], cap_graph[rev_v][j][2] + path_flow, cap_graph[rev_v][j][3])
                        break
                v = u
                
            max_flow += path_flow
        
        return max_flow
    
    # Check if total demand exceeds total capacity
    total_demand = sum(d for _, _, d in streams)
    total_capacity = sum(capacity)
    
    if total_demand > total_capacity:
        print("NO")
        return
    
    # First check if overall flow is possible
    # Create super source (0) and super sink (n+1)
    cap_graph_check = [[] for _ in range(n + 2)]
    
    # Connect super source to all ingress nodes
    ingress_count = defaultdict(int)
    egress_count = defaultdict(int)
    
    for s, t, d in streams:
        ingress_count[s] += d
        egress_count[t] += d
    
    # Add edges from super source to ingress nodes
    for node, demand in ingress_count.items():
        cap_graph_check[0].append((node, -1, demand, -1))
        if node < len(cap_graph_check):
            temp = len(cap_graph_check[node])
        else:
            # Make sure we have enough space
            while len(cap_graph_check) <= node:
                cap_graph_check.append([])
            temp = len(cap_graph_check[node])
        cap_graph_check[node].append((0, -1, 0, -1))  # Reverse edge
    
    # Add edges from egress nodes to super sink
    for node, demand in egress_count.items():
        cap_graph_check[node].append((n+1, -2, demand, -2))
        temp = len(cap_graph_check[n+1])
        cap_graph_check[n+1].append((node, -2, 0, -2))  # Reverse edge
    
    # Add original network edges with infinite capacity for checking
    for i in range(m):
        u, v, cap = edge_info[i]
        cap_graph_check[u].append((v, i, cap, len(cap_graph_check[v])))
        rev_idx = len(cap_graph_check[u]) - 1
        cap_graph_check[v].append((u, rev_idx, 0, i))
    
    # Run max flow to see if all demands can be satisfied
    max_flow = ford_fulkerson(cap_graph_check, 0, n+1)
    total_required = sum(d for _, _, d in streams)
    
    if max_flow < total_required:
        print("NO")
        return
    
    # Now decompose into individual flows
    # For each stream, find a path and push flow
    result = [[0] * m for _ in range(k)]
    
    # Create residual graph for flow decomposition
    res_graph = [[] for _ in range(n + 1)]
    res_capacity = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize with full capacity
    for i in range(m):
        u, v, cap = edge_info[i]
        res_capacity[u][v] = cap
    
    # For each stream, find flow path and update residual graph
    for stream_idx in range(k):
        s, t, d = streams[stream_idx]
        
        # Find d paths from s to t using DFS and residual capacities
        flow_to_send = d
        while flow_to_send > 0:
            # DFS to find a path
            parent = [-1] * (n + 1)
            visited = [False] * (n + 1)
            stack = [s]
            visited[s] = True
            found = False
            
            while stack and not found:
                u = stack.pop()
                if u == t:
                    found = True
                    break
                    
                for v in range(1, n + 1):
                    if res_capacity[u][v] > 0 and not visited[v]:
                        visited[v] = True
                        parent[v] = u
                        stack.append(v)
            
            if not found:
                print("NO")
                return
                
            # Reconstruct path and find bottleneck
            path = []
            cur = t
            while parent[cur] != -1:
                prev = parent[cur]
                path.append((prev, cur))
                cur = prev
            path.reverse()
            
            # Send 1 unit of flow (since we're dealing with integer flows)
            for u, v in path:
                result[stream_idx][edge_map[(u, v)]] += 1
                res_capacity[u][v] -= 1
                res_capacity[v][u] += 1  # Residual back edge
            
            flow_to_send -= 1
    
    # Verify constraints
    for i in range(m):
        total_on_edge = sum(result[j][i] for j in range(k))
        if total_on_edge > capacity[i]:
            print("NO")
            return
    
    print("YES")
    for i in range(k):
        print(' '.join(map(str, result[i])))

solve()