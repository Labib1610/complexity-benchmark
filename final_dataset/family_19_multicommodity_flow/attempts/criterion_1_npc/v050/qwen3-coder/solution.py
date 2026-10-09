from collections import defaultdict, deque

def solve():
    n, m, k = map(int, input().split())
    
    mandates = []
    for i in range(k):
        s, t, d = map(int, input().split())
        mandates.append((s, t, d))
    
    edges = []
    edge_dict = {}
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v, cap))
        edge_dict[(u, v)] = i
    
    # Build graph
    graph = defaultdict(list)
    for u, v, cap in edges:
        graph[u].append(v)
        graph[v].append(u)  # For finding paths, we need bidirectional connectivity info
    
    # For each mandate, find paths from source to target
    paths = []
    for s, t, d in mandates:
        # BFS to find a path from s to t
        queue = deque([(s, [s])])
        visited = set([s])
        path_found = None
        while queue:
            node, path = queue.popleft()
            if node == t:
                path_found = path
                break
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        if not path_found:
            print("NO")
            return
        paths.append(path_found)
    
    # Convert paths to edge usage
    mandate_flows = []
    for i, path in enumerate(paths):
        s, t, d = mandates[i]
        flow = [0] * m
        for j in range(len(path) - 1):
            u, v = path[j], path[j+1]
            if (u, v) in edge_dict:
                idx = edge_dict[(u, v)]
                flow[idx] += d
            else:
                # This shouldn't happen if we found a valid path
                print("NO")
                return
        mandate_flows.append(flow)
    
    # Check if this solution is valid (no edge over capacity)
    total_flow = [0] * m
    for flow in mandate_flows:
        for i in range(m):
            total_flow[i] += flow[i]
    
    for i in range(m):
        if total_flow[i] > edges[i][2]:
            print("NO")
            return
    
    print("YES")
    for flow in mandate_flows:
        print(' '.join(map(str, flow)))

solve()