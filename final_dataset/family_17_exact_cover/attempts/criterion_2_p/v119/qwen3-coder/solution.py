from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for bipartite graph
    # Left side: 1 to q (Zone A)
    # Right side: q+1 to 2*q (Zone B)
    adj = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using Ford-Fulkerson with BFS (Edmonds-Karp)
    # Create a mapping for right side nodes to indices
    match_left = [0] * (q + 1)  # match_left[a] = b if a is matched to b
    match_right = [0] * (q + 1)  # match_right[b-q] = a if b is matched to a
    
    def bfs():
        # Find augmenting path
        queue = deque()
        parent = [-1] * (q + 1)  # parent[a] for nodes in left side
        visited = [False] * (q + 1)
        
        # Initialize queue with all unmatched left nodes
        for a in range(1, q + 1):
            if match_left[a] == 0:
                queue.append(a)
                parent[a] = -2  # Special marker for root
                visited[a] = True
        
        found = False
        final_b = -1
        
        while queue and not found:
            a = queue.popleft()
            
            for b in adj[a]:
                b_idx = b - q  # Convert to 1-based index in right side
                
                # If b is already matched
                if match_right[b_idx] != 0:
                    # Check the partner of b
                    a_next = match_right[b_idx]
                    if not visited[a_next]:
                        visited[a_next] = True
                        parent[a_next] = a
                        queue.append(a_next)
                else:
                    # Found an augmenting path ending at b
                    found = True
                    final_b = b
                    last_a = a
                    break
        
        if not found:
            return False
        
        # Update matching along the augmenting path
        a = last_a
        b = final_b
        b_idx = b - q
        
        # Backtrack to update matches
        while parent[a] != -2:
            prev_a = parent[a]
            prev_b = match_left[a]
            
            # Update matches
            match_left[a] = b
            match_right[b_idx] = a
            
            if prev_b != 0:
                prev_b_idx = prev_b - q
                match_right[prev_b_idx] = 0
            
            a = prev_a
            b = prev_b
            if b != 0:
                b_idx = b - q
        
        # Final update for the last edge
        match_left[a] = final_b
        match_right[final_b - q] = a
        
        return True
    
    # Run matching algorithm
    matching = 0
    while bfs():
        matching += 1
    
    if matching < q:
        print("NO")
        return
    
    print("YES")
    for a in range(1, q + 1):
        print(a, match_left[a])

solve()