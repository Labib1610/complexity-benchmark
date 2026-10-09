from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    _ = int(data[idx])
    idx += 1
    
    s = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    d = int(data[idx])
    idx += 1
    
    edges = []
    graph = defaultdict(list)
    capacity = []
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        c = int(data[idx])
        idx += 1
        edges.append((u, v, c))
        graph[u].append((v, len(capacity)))
        capacity.append(c)
        graph[v].append((u, len(capacity)))
        capacity.append(0)
    
    def bfs(source, sink, parent):
        visited = [False] * (n + 1)
        queue = deque([source])
        visited[source] = True
        parent[source] = -1
        
        while queue:
            u = queue.popleft()
            for v, edge_index in graph[u]:
                if not visited[v] and capacity[edge_index] > 0:
                    queue.append(v)
                    parent[v] = edge_index
                    visited[v] = True
                    if v == sink:
                        return True
        return False
    
    def ford_fulkerson(source, sink):
        parent = [-1] * (n + 1)
        max_flow = 0
        
        while bfs(source, sink, parent):
            path_flow = float('Inf')
            s_node = sink
            while s_node != source:
                edge_index = parent[s_node]
                path_flow = min(path_flow, capacity[edge_index])
                s_node = edges[edge_index//2][0] if edge_index % 2 == 0 else edges[edge_index//2][1]
            
            v = sink
            while v != source:
                edge_index = parent[v]
                capacity[edge_index] -= path_flow
                # Backward edge index: if edge_index is even, backward is edge_index+1, else edge_index-1
                if edge_index % 2 == 0:
                    capacity[edge_index + 1] += path_flow
                    v = edges[edge_index//2][0]
                else:
                    capacity[edge_index - 1] += path_flow
                    v = edges[edge_index//2][1]
            
            max_flow += path_flow
        
        return max_flow
    
    # Create a super source and super sink
    super_source = 0
    super_sink = n + 1
    
    # Add edge from super_source to s with capacity d
    graph[super_source].append((s, len(capacity)))
    capacity.append(d)
    graph[s].append((super_source, len(capacity)))
    capacity.append(0)
    
    # Add edge from t to super_sink with capacity d
    graph[t].append((super_sink, len(capacity)))
    capacity.append(d)
    graph[super_sink].append((t, len(capacity)))
    capacity.append(0)
    
    max_flow = ford_fulkerson(super_source, super_sink)
    
    if max_flow < d:
        print("NO")
        return
    
    print("YES")
    result = []
    for i in range(m):
        # The forward edge is at index 2*i, backward edge at 2*i+1
        # Original capacity - residual capacity = flow
        flow = edges[i][2] - capacity[2*i]
        result.append(str(flow))
    
    print(" ".join(result))

solve()