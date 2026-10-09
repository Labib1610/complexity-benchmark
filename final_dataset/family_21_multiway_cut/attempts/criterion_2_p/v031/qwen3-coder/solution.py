import sys
from collections import defaultdict, deque

def solve():
    n, m, s, t, B = map(int, input().split())
    
    # Build adjacency list representation
    graph = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    # Function to find minimum cut using Ford-Fulkerson with BFS (Edmonds-Karp)
    def bfs_find_path(source, sink, capacity_graph):
        parent = {}
        visited = set()
        queue = deque([source])
        visited.add(source)
        parent[source] = None
        
        while queue:
            node = queue.popleft()
            
            if node == sink:
                break
                
            for neighbor, cap in capacity_graph[node]:
                if neighbor not in visited and cap > 0:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        if sink not in visited:
            return None
            
        # Reconstruct path
        path = []
        current = sink
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        
        return path
    
    # Create residual graph for max flow
    residual = defaultdict(lambda: defaultdict(int))
    edge_map = {}  # Maps (u,v) or (v,u) to original edge index
    
    for i, (u, v, w) in enumerate(edges):
        residual[u][v] += w
        residual[v][u] += w
        edge_map[(u, v)] = i
        edge_map[(v, u)] = i
    
    # Edmonds-Karp algorithm to find max flow/min cut
    def max_flow(source, sink):
        total_flow = 0
        
        while True:
            # Find augmenting path using BFS
            parent = {}
            visited = set()
            queue = deque([source])
            visited.add(source)
            parent[source] = None
            
            found_sink = False
            while queue:
                node = queue.popleft()
                
                if node == sink:
                    found_sink = True
                    break
                    
                for neighbor in residual[node]:
                    if neighbor not in visited and residual[node][neighbor] > 0:
                        visited.add(neighbor)
                        parent[neighbor] = node
                        queue.append(neighbor)
            
            if not found_sink:
                break
                
            # Find bottleneck capacity along path
            path_flow = float('inf')
            current = sink
            path_edges = []
            
            while parent[current] is not None:
                prev = parent[current]
                path_flow = min(path_flow, residual[prev][current])
                path_edges.append((prev, current))
                current = prev
            
            # Update residual capacities
            current = sink
            while parent[current] is not None:
                prev = parent[current]
                residual[prev][current] -= path_flow
                residual[current][prev] += path_flow
                current = prev
            
            total_flow += path_flow
        
        return total_flow
    
    # Check if s and t are connected at all
    def is_connected(source, sink):
        visited = set()
        stack = [source]
        visited.add(source)
        
        while stack:
            node = stack.pop()
            if node == sink:
                return True
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return False
    
    # If s and t aren't connected, we're done
    if not is_connected(s, t):
        print("YES")
        print("0")
        return
    
    # Calculate minimum cut
    min_cut_value = max_flow(s, t)
    
    if min_cut_value > B:
        print("NO")
        return
    
    # Now we need to identify which edges form the cut
    # Run BFS from s in residual graph to find reachable nodes
    visited_from_s = set()
    queue = deque([s])
    visited_from_s.add(s)
    
    while queue:
        node = queue.popleft()
        for neighbor in residual[node]:
            if neighbor not in visited_from_s and residual[node][neighbor] > 0:
                visited_from_s.add(neighbor)
                queue.append(neighbor)
    
    # Edges crossing the cut
    cut_edges = []
    removed_indices = []
    
    for i, (u, v, w) in enumerate(edges):
        # Edge goes from S-side to T-side
        if u in visited_from_s and v not in visited_from_s:
            cut_edges.append((u, v))
            removed_indices.append(i)
        elif v in visited_from_s and u not in visited_from_s:
            cut_edges.append((v, u))  # Keep consistent direction
            removed_indices.append(i)
    
    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(u, v)

solve()