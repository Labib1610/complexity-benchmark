import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    trios = []
    for _ in range(t):
        s = int(next(it))
        c = int(next(it))
        f = int(next(it))
        trios.append((s - 1, c - 1, f - 1))
    
    # Build bipartite graph: left side = starters (0..k-1), right side = finales (0..k-1)
    # Edge (s, f) exists if there's a trio (s, c, f) for some c
    # We need to find a perfect matching where each matched edge (s, f) is assigned
    # a unique centerpiece c
    
    # Group trios by (s, f) pair, keeping track of available centerpieces
    from collections import defaultdict
    sf_to_c = defaultdict(list)
    for idx, (s, c, f) in enumerate(trios):
        sf_to_c[(s, f)].append(c)
    
    # Build adjacency list for bipartite graph
    adj = [[] for _ in range(k)]
    for (s, f), cs in sf_to_c.items():
        adj[s].append(f)
    
    # Find maximum matching using Hopcroft-Karp
    def hopcroft_karp():
        pair_u = [-1] * k
        pair_v = [-1] * k
        dist = [0] * k
        
        from collections import deque
        
        def bfs():
            queue = deque()
            for u in range(k):
                if pair_u[u] == -1:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = float('inf')
            dist_null = float('inf')
            while queue:
                u = queue.popleft()
                if dist[u] < dist_null:
                    for v in adj[u]:
                        if pair_v[v] == -1:
                            dist_null = dist[u] + 1
                        elif dist[pair_v[v]] == float('inf'):
                            dist[pair_v[v]] = dist[u] + 1
                            queue.append(pair_v[v])
            return dist_null != float('inf')
        
        def dfs(u):
            for v in adj[u]:
                if pair_v[v] == -1 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
            dist[u] = float('inf')
            return False
        
        matching = 0
        while bfs():
            for u in range(k):
                if pair_u[u] == -1:
                    if dfs(u):
                        matching += 1
        return pair_u, pair_v, matching
    
    pair_u, pair_v, matching = hopcroft_karp()
    
    if matching != k:
        print("NO")
        return
    
    # We have a perfect matching. Now we need to assign centerpieces.
    # For each matched pair (s, f), we need to assign a unique c.
    # This is equivalent to finding a matching in a bipartite graph where
    # left side = matched pairs (s, f), right side = centerpieces c
    
    # Create list of matched pairs
    matched_pairs = []
    for s in range(k):
        f = pair_u[s]
        matched_pairs.append((s, f))
    
    # Build bipartite graph for centerpiece assignment
    # Left node i corresponds to matched_pairs[i] = (s, f)
    # Edge from i to c exists if (s, c, f) is a valid trio
    
    # Build adjacency: for each matched pair, which centerpieces are available?
    c_adj = [[] for _ in range(k)]
    for i, (s, f) in enumerate(matched_pairs):
        for c in sf_to_c[(s, f)]:
            c_adj[i].append(c)
    
    # Find matching in this graph
    def find_c_matching():
        pair_c_left = [-1] * k  # which c is assigned to left node i
        pair_c_right = [-1] * k  # which left node is assigned to c
        
        def dfs_c(u, visited):
            for v in c_adj[u]:
                if visited[v]:
                    continue
                visited[v] = True
                if pair_c_right[v] == -1 or dfs_c(pair_c_right[v], visited):
                    pair_c_left[u] = v
                    pair_c_right[v] = u
                    return True
            return False
        
        for u in range(k):
            visited = [False] * k
            if not dfs_c(u, visited):
                return None
        
        return pair_c_left
    
    c_assignment = find_c_matching()
    
    if c_assignment is None:
        print("NO")
        return
    
    # Output result
    print("YES")
    for i, (s, f) in enumerate(matched_pairs):
        c = c_assignment[i]
        print(f"{s + 1} {c + 1} {f + 1}")

solve()