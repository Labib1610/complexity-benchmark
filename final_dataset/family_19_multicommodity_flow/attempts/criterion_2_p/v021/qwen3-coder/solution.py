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
    asset_type = int(data[idx])
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
        graph[u].append((v, i))
        graph[v].append((u, i))
        capacity.append(cap)
    
    # We need to find a flow of value d from s to t
    # This is a max flow problem with given capacities
    
    # Build adjacency list for residual graph
    # We'll use Ford-Fulkerson with BFS (Edmonds-Karp)
    
    def bfs():
        parent = [-1] * (n + 1)
        visited = [False] * (n + 1)
        queue = deque([s])
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            for v, edge_idx in graph[u]:
                if not visited[v] and flow[edge_idx] < capacity[edge_idx]:
                    visited[v] = True
                    parent[v] = (u, edge_idx)
                    queue.append(v)
                    if v == t:
                        return parent
        return None
    
    # Initialize flow
    flow = [0] * m
    max_flow = 0
    
    while max_flow < d:
        parent = bfs()
        if parent is None or not visited[t]:
            break
            
        # Find minimum residual capacity along the path
        path_flow = d - max_flow
        v = t
        while v != s:
            u, edge_idx = parent[v]
            path_flow = min(path_flow, capacity[edge_idx] - flow[edge_idx])
            v = u
            
        # Update flow
        v = t
        while v != s:
            u, edge_idx = parent[v]
            flow[edge_idx] += path_flow
            v = u
            
        max_flow += path_flow
    
    if max_flow >= d:
        print("YES")
        print(' '.join(map(str, flow)))
    else:
        print("NO")

solve()