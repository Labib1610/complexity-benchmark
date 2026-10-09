from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for bipartite graph
    # Left side: terrestrial arrays (1 to q)
    # Right side: orbital relays (q+1 to 2q)
    adj = defaultdict(list)
    degree = [0] * (2 * q + 1)
    
    edges = []
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
        degree[a] += 1
        degree[b] += 1
        edges.append((a, b))
    
    # Check if a perfect matching exists using Hall's theorem approach
    # But we'll use a more direct approach: try to find maximum matching
    
    # Use Hopcroft-Karp or simpler Ford-Fulkerson based approach
    # Since we need exactly q edges in a matching, let's use a standard bipartite matching algorithm
    
    match_terrestrial = [-1] * (q + 1)  # match_terrestrial[i] = matched orbital relay for terrestrial i
    match_orbital = [-1] * (2 * q + 1)  # match_orbital[j] = matched terrestrial array for orbital j
    
    def bfs():
        queue = deque()
        dist = [-1] * (q + 1)
        
        for i in range(1, q + 1):
            if match_terrestrial[i] == -1:
                dist[i] = 0
                queue.append(i)
            else:
                dist[i] = -1
        
        found = False
        while queue:
            u = queue.popleft()
            
            for v in adj[u]:
                if match_orbital[v] != -1 and match_orbital[v] != u:
                    paired_u = match_orbital[v]
                    if dist[paired_u] == -1:
                        dist[paired_u] = dist[u] + 1
                        queue.append(paired_u)
                elif match_orbital[v] == -1:
                    found = True
        
        return found
    
    def dfs(u):
        for v in adj[u]:
            if match_orbital[v] != -1 and match_orbital[v] != u:
                paired_u = match_orbital[v]
                if dist[paired_u] == dist[u] + 1 and dfs(paired_u):
                    match_terrestrial[u] = v
                    match_orbital[v] = u
                    return True
            elif match_orbital[v] == -1:
                match_terrestrial[u] = v
                match_orbital[v] = u
                return True
        return False
    
    # Simplified approach: use a greedy matching first, then augmenting paths
    def find_matching():
        matched = 0
        
        # Greedy matching
        used_orbital = [False] * (2 * q + 1)
        for i in range(1, q + 1):
            for j in adj[i]:
                if not used_orbital[j]:
                    match_terrestrial[i] = j
                    match_orbital[j] = i
                    used_orbital[j] = True
                    matched += 1
                    break
        
        # Try to improve with augmenting paths
        while True:
            changed = False
            
            # Reset dist array
            dist = [-1] * (q + 1)
            queue = deque()
            
            # Find free nodes on terrestrial side
            for i in range(1, q + 1):
                if match_terrestrial[i] == -1:
                    dist[i] = 0
                    queue.append(i)
            
            # BFS to find shortest augmenting paths
            while queue:
                u = queue.popleft()
                
                for v in adj[u]:
                    matched_terrestrial = match_orbital[v]
                    if matched_terrestrial != -1 and matched_terrestrial != u:
                        if dist[matched_terrestrial] == -1:
                            dist[matched_terrestrial] = dist[u] + 1
                            queue.append(matched_terrestrial)
            
            # DFS to find augmenting paths
            visited = [False] * (q + 1)
            def dfs_path(u):
                if visited[u]:
                    return False
                visited[u] = True
                
                for v in adj[u]:
                    matched_terrestrial = match_orbital[v]
                    if matched_terrestrial == -1:
                        # Found an augmenting path
                        match_terrestrial[u] = v
                        match_orbital[v] = u
                        return True
                    elif matched_terrestrial != u:
                        if dist[matched_terrestrial] == dist[u] + 1 and dfs_path(matched_terrestrial):
                            match_terrestrial[u] = v
                            match_orbital[v] = u
                            return True
                return False
            
            # Try to find augmenting paths from free terrestrial nodes
            for i in range(1, q + 1):
                if match_terrestrial[i] == -1:
                    visited = [False] * (q + 1)
                    if dfs_path(i):
                        matched += 1
                        changed = True
            
            if not changed:
                break
        
        return matched == q
    
    # For large inputs, let's use a simpler approach
    # Build residual graph and find max flow
    if find_matching():
        print("YES")
        for i in range(1, q + 1):
            print(i, match_terrestrial[i])
    else:
        print("NO")

solve()