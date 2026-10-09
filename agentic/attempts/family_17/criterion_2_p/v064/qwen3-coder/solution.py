from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build bipartite graph
    # Left side: power modules 1 to q
    # Right side: habitation modules q+1 to 2q
    graph = defaultdict(list)
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    # Try to find a maximum matching using BFS (Hopcroft-Karp like approach)
    # But since we need a perfect matching, we can use a simpler approach
    
    # For each power module, try to assign it to an available habitation module
    match_power = [0] * (q + 1)  # match_power[i] = which habitation module power i is matched to
    match_hab = [0] * (q + 1)    # match_hab[j] = which power module habitation j is matched to
    
    def bfs():
        # Find augmenting paths
        visited = [False] * (q + 1)
        parent = [-1] * (q + 1)
        queue = deque()
        
        # Initialize queue with unmatched power modules
        for i in range(1, q + 1):
            if match_power[i] == 0:
                visited[i] = True
                parent[i] = -1
                queue.append(i)
        
        found_path = False
        end_node = -1
        
        while queue and not found_path:
            u = queue.popleft()
            
            # Check all neighbors of u
            for v in graph[u]:
                v_idx = v - q  # Convert to 1-based index in habitation array
                
                if match_hab[v_idx] == 0:
                    # Found an augmenting path
                    found_path = True
                    end_node = u
                    final_v = v
                    break
                    
                # Otherwise, this habitation module is matched to some power module
                next_u = match_hab[v_idx]
                if not visited[next_u]:
                    visited[next_u] = True
                    parent[next_u] = u
                    queue.append(next_u)
        
        if not found_path:
            return False
            
        # Update the matching along the augmenting path
        current = end_node
        next_v = final_v
        
        while current != -1:
            current_v_idx = next_v - q
            prev_match = match_power[current]
            
            match_power[current] = next_v
            match_hab[current_v_idx] = current
            
            if prev_match != 0:
                prev_v_idx = prev_match - q
                match_hab[prev_v_idx] = 0
                
            next_v = prev_match
            current = parent[current]
            
        return True
    
    # Keep finding augmenting paths until no more can be found
    matching = 0
    while bfs():
        matching += 1
    
    if matching < q:
        print("NO")
    else:
        print("YES")
        for i in range(1, q + 1):
            print(i, match_power[i])

solve()