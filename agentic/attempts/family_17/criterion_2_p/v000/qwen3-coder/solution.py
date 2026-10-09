from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for bipartite graph
    # Controllers: 1 to q
    # Platforms: q+1 to 2*q
    graph = defaultdict(list)
    adj = defaultdict(list)
    
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    # Try to find a maximum matching using BFS-based approach (Hopcroft-Karp like)
    # But we'll use a simpler approach: try to find a perfect matching
    
    # For bipartite matching
    match_controller = [0] * (q + 1)  # match_controller[c] = matched platform
    match_platform = [0] * (q + 1)    # match_platform[p] = matched controller
    
    def bfs():
        queue = deque()
        dist = [0] * (q + 1)
        
        for c in range(1, q + 1):
            if match_controller[c] == 0:
                dist[c] = 0
                queue.append(c)
            else:
                dist[c] = float('inf')
        
        dist[0] = float('inf')
        
        while queue:
            c = queue.popleft()
            
            if dist[c] < dist[0]:
                for p in adj[c]:
                    p_idx = p - q  # Convert platform id to 1-based index
                    if dist[match_platform[p_idx]] == 0:
                        dist[match_platform[p_idx]] = dist[c] + 1
                        queue.append(match_platform[p_idx])
        
        return dist[0] != float('inf')
    
    def dfs(c):
        if c != 0:
            for p in adj[c]:
                p_idx = p - q
                if dist[match_platform[p_idx]] == dist[c] + 1:
                    if dfs(match_platform[p_idx]):
                        match_platform[p_idx] = c
                        match_controller[c] = p
                        return True
            dist[c] = float('inf')
            return False
        return True
    
    # Main matching algorithm
    matching = 0
    dist = [0] * (q + 1)
    
    # Use a simpler approach: greedy matching with backtracking
    def find_matching():
        # Try to build matching incrementally
        used_controller = [False] * (q + 1)
        used_platform = [False] * (q + 1)
        matching_pairs = []
        
        def backtrack(controller):
            if controller > q:
                return True
                
            for platform in adj[controller]:
                p_idx = platform - q
                if not used_platform[p_idx]:
                    used_controller[controller] = True
                    used_platform[p_idx] = True
                    matching_pairs.append((controller, platform))
                    
                    if backtrack(controller + 1):
                        return True
                    
                    matching_pairs.pop()
                    used_controller[controller] = False
                    used_platform[p_idx] = False
            
            return False
        
        # This might be too slow, let's try a different approach
        # Use a greedy approach with augmenting paths
        
        # Reset
        for c in range(1, q + 1):
            match_controller[c] = 0
        for p in range(1, q + 1):
            match_platform[p] = 0
            
        # Greedy initial matching
        for c in range(1, q + 1):
            for p in adj[c]:
                p_idx = p - q
                if match_platform[p_idx] == 0:
                    match_controller[c] = p
                    match_platform[p_idx] = c
                    break
        
        # Try to improve with augmenting paths
        while bfs():
            for c in range(1, q + 1):
                if match_controller[c] == 0:
                    dfs(c)
        
        # Check if we have a perfect matching
        count = sum(1 for c in range(1, q + 1) if match_controller[c] != 0)
        return count == q
    
    # Even simpler: use a standard implementation of bipartite matching
    def max_bipartite_matching():
        match = [-1] * (2 * q + 1)
        
        def bpm(u, seen):
            for v in adj[u]:
                if seen[v]:
                    continue
                seen[v] = True
                
                if match[v] == -1 or bpm(match[v], seen):
                    match[v] = u
                    match[u] = v
                    return True
            return False
        
        result = 0
        for i in range(1, q + 1):
            seen = [False] * (2 * q + 1)
            if bpm(i, seen):
                result += 1
        
        # Store the matching for output
        pairs = []
        for c in range(1, q + 1):
            if match[c] != -1:
                pairs.append((c, match[c]))
        
        return result == q, pairs
    
    # Let's implement Hopcroft-Karp properly
    def hopcroft_karp():
        pair_u = [0] * (q + 1)
        pair_v = [0] * (q + 1)
        dist = [0] * (q + 1)
        
        def bfs_hk():
            queue = deque()
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
                        v_idx = v - q
                        if dist[pair_v[v_idx]] == float('inf'):
                            dist[pair_v[v_idx]] = dist[u] + 1
                            queue.append(pair_v[v_idx])
            return dist[0] != float('inf')
        
        def dfs_hk(u):
            if u != 0:
                for v in adj[u]:
                    v_idx = v - q
                    if dist[pair_v[v_idx]] == dist[u] + 1:
                        if dfs_hk(pair_v[v_idx]):
                            pair_v[v_idx] = u
                            pair_u[u] = v
                            return True
                dist[u] = float('inf')
                return False
            return True
        
        matching = 0
        while bfs_hk():
            for u in range(1, q + 1):
                if pair_u[u] == 0:
                    if dfs_hk(u):
                        matching += 1
        
        # Check if perfect matching
        if matching == q:
            pairs = []
            for u in range(1, q + 1):
                if pair_u[u] != 0:
                    pairs.append((u, pair_u[u]))
            return True, pairs
        return False, []
    
    # For small inputs, we can try a backtracking approach
    if q <= 1000:  # Adjust threshold as needed
        result, pairs = hopcroft_karp()
    else:
        result, pairs = hopcroft_karp()
    
    if result:
        print("YES")
        for c, p in pairs:
            print(c, p)
    else:
        print("NO")

solve()