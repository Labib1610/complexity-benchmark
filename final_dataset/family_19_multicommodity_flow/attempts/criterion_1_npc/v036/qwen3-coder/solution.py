from collections import defaultdict, deque

def solve():
    n, m, k = map(int, input().split())
    
    orders = []
    for i in range(k):
        s, t, d = map(int, input().split())
        orders.append((s, t, d))
    
    edges = []
    edge_index = {}
    graph = defaultdict(list)
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v, cap))
        edge_index[(u, v)] = i
        graph[u].append((v, i))
        graph[v].append((u, i))  # For flow calculation
    
    # For each order, we need to find a feasible flow
    # We'll use a min-cost max-flow approach or simply path decomposition
    
    # Let's build a flow network for each order separately and find paths
    result = [[0] * m for _ in range(k)]
    total_flow = [0] * m  # To track total usage of each edge
    
    def find_paths(source, target, amount):
        # Find 'amount' number of paths from source to target using DFS
        # Returns list of paths, each path is a list of edge indices
        paths = []
        
        def dfs(node, target, visited, path_edges):
            if node == target:
                return [path_edges[:]]
            
            all_paths = []
            for neighbor, edge_idx in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    path_edges.append(edge_idx)
                    sub_paths = dfs(neighbor, target, visited, path_edges)
                    all_paths.extend(sub_paths)
                    path_edges.pop()
                    visited.remove(neighbor)
                    
                    # Early termination if we have enough paths
                    if len(all_paths) >= amount:
                        break
            
            return all_paths[:amount]
        
        # Try to find amount paths
        visited = {source}
        all_paths = dfs(source, target, visited, [])
        
        return all_paths[:amount] if len(all_paths) >= amount else []
    
    # Check if solution exists
    for i, (s, t, d) in enumerate(orders):
        # For this simple case, we can try to decompose into unit flows
        # and then scale up. But for general case, we need to be more careful.
        
        # Let's use a different approach: model as min-cost flow
        # But since all costs are 1, we just need any feasible flow
        
        # Use Ford-Fulkerson with path finding
        # But we need to be careful about multiple orders sharing edges
        
        # Simple approach: for each unit of flow, find a path
        paths = find_paths(s, t, d)
        if len(paths) < d:
            print("NO")
            return
            
        # Distribute the flow
        for path in paths:
            for edge_idx in path:
                result[i][edge_idx] += 1
                total_flow[edge_idx] += 1
    
    # Check capacity constraints
    for j in range(m):
        if total_flow[j] > edges[j][2]:  # exceed capacity
            print("NO")
            return
    
    print("YES")
    for i in range(k):
        print(' '.join(map(str, result[i])))

solve()