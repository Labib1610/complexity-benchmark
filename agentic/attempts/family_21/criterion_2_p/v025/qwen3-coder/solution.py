import sys
from collections import defaultdict, deque

def read_input():
    n, m, s, t, B = map(int, sys.stdin.readline().split())
    edges = []
    edge_dict = {}
    graph = defaultdict(list)
    
    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w, i))
        edge_dict[(u, v)] = (w, i)
        edge_dict[(v, u)] = (w, i)
        graph[u].append((v, w, i))
        graph[v].append((u, w, i))
    
    return n, m, s, t, B, edges, edge_dict, graph

def bfs_check_connectivity(graph, n, source, target):
    if source == target:
        return True
    
    visited = [False] * (n + 1)
    queue = deque([source])
    visited[source] = True
    
    while queue:
        node = queue.popleft()
        for neighbor, _, _ in graph[node]:
            if neighbor == target:
                return True
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return False

def find_min_cut(graph, n, source, target):
    # Using Ford-Fulkerson with BFS (Edmonds-Karp) to find max flow/min cut
    # We'll implement a simplified version for unit flows
    
    def bfs_flow_path():
        parent = [-1] * (n + 1)
        parent_edge = [-1] * (n + 1)
        visited = [False] * (n + 1)
        
        queue = deque([(source, None)])
        visited[source] = True
        
        while queue:
            current, edge_idx = queue.popleft()
            
            if current == target:
                path = []
                curr = target
                while parent[curr] != -1:
                    path.append(parent_edge[curr])
                    curr = parent[curr]
                return list(reversed(path))
            
            for neighbor, weight, edge_id in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = current
                    parent_edge[neighbor] = edge_id
                    queue.append((neighbor, edge_id))
        
        return None
    
    # For this problem, we need to find minimum weight cut
    # Let's use a different approach - find all paths and then solve set cover
    
    # Actually, let's model this as finding minimum cut in weighted graph
    # We can use Stoer-Wagner algorithm variant or reduce to max flow
    
    # Since this is small scale, let's try a greedy approach with connectivity check
    
    return None

def solve():
    n, m, s, t, B, edges, edge_dict, graph = read_input()
    
    # Check if s and t are already disconnected
    if not bfs_check_connectivity(graph, n, s, t):
        print("YES")
        print(0)
        return
    
    # We need to find minimum weight set of edges to remove to disconnect s and t
    # This is the minimum cut problem
    
    # Let's implement a simple flow-based solution
    # But since weights matter, we need to be careful
    
    # Create residual graph for flow algorithm
    res_graph = defaultdict(dict)
    edge_index_map = {}  # Maps (u,v) to edge index
    
    for i, (u, v, w, idx) in enumerate(edges):
        # For undirected graph, we add edges in both directions
        if v not in res_graph[u]:
            res_graph[u][v] = {'cap': w, 'flow': 0}
        else:
            res_graph[u][v]['cap'] += w
            
        if u not in res_graph[v]:
            res_graph[v][u] = {'cap': w, 'flow': 0}
        else:
            res_graph[v][u]['cap'] += w
            
        edge_index_map[(u,v)] = i
        edge_index_map[(v,u)] = i
    
    # Implement Ford-Fulkerson with DFS
    def dfs_find_augmenting_path(source, sink, visited, min_flow):
        if source == sink:
            return min_flow, []
        
        visited.add(source)
        
        for neighbor in res_graph[source]:
            edge = res_graph[source][neighbor]
            if neighbor not in visited and edge['cap'] > edge['flow']:
                bottleneck = min(min_flow, edge['cap'] - edge['flow'])
                result_flow, path = dfs_find_augmenting_path(neighbor, sink, visited, bottleneck)
                if result_flow > 0:
                    path.append((source, neighbor))
                    return result_flow, path
        
        return 0, []
    
    # Max flow algorithm
    max_flow = 0
    cut_edges = set()
    
    while True:
        visited = set()
        flow, path = dfs_find_augmenting_path(s, t, visited, float('inf'))
        
        if flow == 0:
            break
            
        max_flow += flow
        
        # Update residual capacities
        for u, v in path:
            res_graph[u][v]['flow'] += flow
            if v in res_graph[u] and u in res_graph[v]:
                res_graph[v][u]['flow'] -= flow
    
    # Now we need to find the actual cut
    # Run BFS from source in residual network to find reachable nodes
    visited_source = set()
    queue = deque([s])
    visited_source.add(s)
    
    while queue:
        node = queue.popleft()
        for neighbor in res_graph[node]:
            edge = res_graph[node][neighbor]
            # If there's still capacity, we can reach neighbor
            if edge['cap'] > edge['flow'] and neighbor not in visited_source:
                visited_source.add(neighbor)
                queue.append(neighbor)
    
    # Find edges crossing the cut
    selected_edges = []
    total_cost = 0
    
    for u, v, w, idx in edges:
        # Edge goes from S-side to T-side
        if u in visited_source and v not in visited_source:
            selected_edges.append((u, v))
            total_cost += w
        elif v in visited_source and u not in visited_source:
            selected_edges.append((v, u))  # Keep consistent orientation
            total_cost += w
    
    # Check if we can afford this cut
    if total_cost <= B:
        print("YES")
        print(len(selected_edges))
        for u, v in selected_edges:
            print(u, v)
    else:
        # Try a greedy approach - find any valid cut within budget
        # Sort edges by weight and try adding them until s and t are disconnected
        
        sorted_edges = sorted(edges, key=lambda x: x[2])  # Sort by weight
        temp_graph = defaultdict(list)
        
        # Build initial graph
        for u, v, w, idx in edges:
            temp_graph[u].append(v)
            temp_graph[v].append(u)
        
        removed_edges = []
        total_weight = 0
        
        def is_connected(graph, start, end, n):
            if start == end:
                return True
            visited = [False] * (n + 1)
            queue = deque([start])
            visited[start] = True
            
            while queue:
                node = queue.popleft()
                if node == end:
                    return True
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            return False
        
        # Remove edges one by one until s and t are disconnected
        for u, v, w, idx in sorted_edges:
            if total_weight + w > B:
                continue
                
            # Temporarily remove edge
            temp_graph[u].remove(v)
            temp_graph[v].remove(u)
            
            # Check if still connected
            if not is_connected(temp_graph, s, t, n):
                # Good, we can keep this removal
                removed_edges.append((u, v))
                total_weight += w
            else:
                # Put edge back
                temp_graph[u].append(v)
                temp_graph[v].append(u)
                
            if not is_connected(temp_graph, s, t, n):
                break
        
        if not is_connected(temp_graph, s, t, n) and total_weight <= B:
            print("YES")
            print(len(removed_edges))
            for u, v in removed_edges:
                print(u, v)
        else:
            print("NO")

solve()