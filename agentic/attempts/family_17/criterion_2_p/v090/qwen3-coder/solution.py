from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build bipartite graph
    # Left side: modules 1 to q
    # Right side: nodes q+1 to 2q
    graph = defaultdict(list)
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    # Try to find a perfect matching using Ford-Fulkerson with BFS (Edmonds-Karp)
    # We'll model this as a flow network:
    # Source (0) -> modules (1..q) -> nodes (q+1..2q) -> sink (2q+1)
    
    def bfs_match():
        # match_node[v] = u means node v (on right) is matched to module u (on left)
        match_module_to_node = [-1] * (q + 1)  # index 0 unused, 1..q for modules
        match_node_to_module = [-1] * (q + 1)  # index 0 unused, 1..q for nodes (q+1 .. 2q mapped to 1..q)
        
        def bfs():
            # Find augmenting path
            queue = deque()
            parent = [-1] * (q + 1)  # For modules
            visited = [False] * (q + 1)  # For modules
            
            # Start BFS from all unmatched modules
            for u in range(1, q + 1):
                if match_module_to_node[u] == -1:
                    queue.append(u)
                    parent[u] = -2  # Special marker for root
                    visited[u] = True
            
            found = -1  # The module we found an augmenting path to
            
            while queue:
                u = queue.popleft()
                
                # Explore neighbors
                for v_original in graph[u]:
                    v = v_original - q  # Map node id to 1..q
                    
                    if match_node_to_module[v] == -1:
                        # Found an augmenting path to an unmatched node
                        found = u
                        parent[v + q] = u  # Store the path
                        break
                    
                    # Otherwise, continue BFS through the matched edge
                    matched_module = match_node_to_module[v]
                    if not visited[matched_module]:
                        visited[matched_module] = True
                        parent[matched_module] = u
                        queue.append(matched_module)
            
            if found == -1:
                return False  # No augmenting path
            
            # Augment along the path
            cur = found
            while cur != -2:
                if cur <= q:  # It's a module
                    # This should be the end of the path
                    break
                else:  # It's a node
                    node_idx = cur - q
                    prev_module = parent[cur]
                    next_module = match_node_to_module[node_idx]
                    
                    # Update matching
                    match_module_to_node[prev_module] = cur
                    match_node_to_module[node_idx] = prev_module
                    
                    cur = parent[prev_module]
            
            return True
        
        # Keep finding augmenting paths until none exist
        matching = 0
        while bfs():
            matching += 1
        
        if matching < q:
            return None  # Not a perfect matching
        
        result = []
        for module in range(1, q + 1):
            node = match_module_to_node[module]
            result.append((module, node))
        
        return result
    
    matching_result = bfs_match()
    
    if matching_result is None:
        print("NO")
    else:
        print("YES")
        for module, node in matching_result:
            print(module, node)

solve()