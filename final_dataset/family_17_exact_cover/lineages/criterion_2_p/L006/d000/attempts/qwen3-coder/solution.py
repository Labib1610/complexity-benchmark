from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build bipartite graph
    # Controllers: 1 to q
    # Platforms: q+1 to 2*q
    graph = defaultdict(list)
    adj = defaultdict(list)
    
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    # Try to find a perfect matching using BFS (Hopcroft-Karp like approach)
    # But we'll use a simpler approach: try to find maximum matching using augmenting paths
    
    # pair_u[u] stores the platform paired with controller u (0 if unmatched)
    # pair_v[v] stores the controller paired with platform v (0 if unmatched)
    pair_u = [0] * (q + 1)
    pair_v = [0] * (q + 1)
    
    def bfs():
        # BFS to find shortest augmenting paths
        dist = [0] * (q + 1)
        queue = deque()
        
        # Initialize queue with all unmatched controllers
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        
        dist[0] = float('inf')
        
        while queue:
            u = queue.popleft()
            
            if dist[u] < dist[0]:
                for v in adj[u]:
                    # v is a platform (q+1 to 2*q), convert to 1-based index
                    v_idx = v - q
                    if dist[pair_v[v_idx]] == float('inf'):
                        dist[pair_v[v_idx]] = dist[u] + 1
                        queue.append(pair_v[v_idx])
        
        return dist[0] != float('inf')
    
    def dfs(u):
        if u == 0:
            return True
            
        for v in adj[u]:
            # v is a platform (q+1 to 2*q), convert to 1-based index
            v_idx = v - q
            if dist[pair_v[v_idx]] == dist[u] + 1:
                if dfs(pair_v[v_idx]):
                    pair_v[v_idx] = u
                    pair_u[u] = v
                    return True
        
        dist[u] = float('inf')
        return False
    
    # Main matching algorithm
    matching = 0
    dist = [0] * (q + 1)
    
    # Simplified approach: use a greedy method first, then try to improve
    # For this problem, let's use a simpler DFS-based approach
    
    def find_matching():
        match = [0] * (q + 1)  # match[controller] = platform
        rev_match = [0] * (q + 1)  # rev_match[platform - q] = controller
        
        def dfs_util(u, visited):
            for v in adj[u]:
                v_idx = v - q
                if visited[v_idx]:
                    continue
                visited[v_idx] = True
                
                # If platform v is free or we can find an augmenting path
                if rev_match[v_idx] == 0 or dfs_util(rev_match[v_idx], visited):
                    match[u] = v
                    rev_match[v_idx] = u
                    return True
            return False
        
        result = 0
        for u in range(1, q + 1):
            visited = [False] * (q + 1)
            if dfs_util(u, visited):
                result += 1
        
        return result, match
    
    matching_size, final_match = find_matching()
    
    if matching_size == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, final_match[u])
    else:
        print("NO")

solve()