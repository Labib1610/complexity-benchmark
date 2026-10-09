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
        cap = int(data[idx])
        idx += 1
        edges.append((u, v))
        graph[u].append((v, len(capacity), cap, 0))  # (to, edge_index, capacity, flow)
        capacity.append(cap)
        graph[v].append((u, len(capacity), 0, 0))    # reverse edge with capacity 0
        capacity.append(0)
    
    # Ford-Fulkerson with BFS (Edmonds-Karp)
    def bfs():
        parent = [-1] * (n + 1)
        edge_index = [-1] * (n + 1)
        visited = [False] * (n + 1)
        queue = deque()
        queue.append(s)
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            for v, idx, cap, flow in graph[u]:
                if not visited[v] and cap > flow:
                    visited[v] = True
                    parent[v] = u
                    edge_index[v] = idx
                    if v == t:
                        return parent, edge_index
                    queue.append(v)
        return None, None
    
    max_flow = 0
    flow_values = [0] * m
    
    while True:
        parent, edge_index = bfs()
        if parent is None:
            break
            
        # Find minimum residual capacity along the path
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            idx = edge_index[v]
            cap = capacity[idx]
            flow = graph[u][idx//2][3] if idx % 2 == 0 else graph[v][idx//2][3]
            path_flow = min(path_flow, cap - flow)
            v = u
            
        if path_flow == 0:
            break
            
        # Update flows
        v = t
        while v != s:
            u = parent[v]
            idx = edge_index[v]
            # Update the actual flow in the graph structure
            if idx % 2 == 0:  # forward edge
                graph[u][idx//2] = (graph[u][idx//2][0], graph[u][idx//2][1], graph[u][idx//2][2], graph[u][idx//2][3] + path_flow)
                graph[v][idx//2 + (1 if idx//2 < len(graph[v]) and graph[v][idx//2][1] == idx+1 else 0)] = (graph[v][idx//2 + (1 if idx//2 < len(graph[v]) and graph[v][idx//2][1] == idx+1 else 0)][0], graph[v][idx//2 + (1 if idx//2 < len(graph[v]) and graph[v][idx//2][1] == idx+1 else 0)][1], graph[v][idx//2 + (1 if idx//2 < len(graph[v]) and graph[v][idx//2][1] == idx+1 else 0)][2], graph[v][idx//2 + (1 if idx//2 < len(graph[v]) and graph[v][idx//2][1] == idx+1 else 0)][3] - path_flow)
            else:  # backward edge
                graph[v][idx//2] = (graph[v][idx//2][0], graph[v][idx//2][1], graph[v][idx//2][2], graph[v][idx//2][3] - path_flow)
                graph[u][idx//2 - (1 if idx//2 > 0 and graph[u][idx//2-1][1] == idx-1 else 0)] = (graph[u][idx//2 - (1 if idx//2 > 0 and graph[u][idx//2-1][1] == idx-1 else 0)][0], graph[u][idx//2 - (1 if idx//2 > 0 and graph[u][idx//2-1][1] == idx-1 else 0)][1], graph[u][idx//2 - (1 if idx//2 > 0 and graph[u][idx//2-1][1] == idx-1 else 0)][2], graph[u][idx//2 - (1 if idx//2 > 0 and graph[u][idx//2-1][1] == idx-1 else 0)][3] + path_flow)
            v = u
            
            # Update flow_values for original edges
            if idx % 2 == 0:
                flow_values[idx//2] += path_flow
            else:
                flow_values[idx//2] -= path_flow
                
        max_flow += path_flow
        if max_flow >= d:
            break
    
    if max_flow >= d:
        print("YES")
        print(' '.join(map(str, flow_values)))
    else:
        print("NO")

solve()