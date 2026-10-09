import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check if graph is 3-regular
    for i in range(1, n + 1):
        if len(adj[i]) != 3:
            print("NO")
            return
    
    # Build adjacency with edge indices
    adj_idx = [[] for _ in range(n + 1)]
    for i in range(n + 1):
        for v, e in adj[i]:
            adj_idx[i].append(e)
    
    # Find a perfect matching using greedy augmentation
    match = [-1] * m
    used = [False] * (n + 1)
    
    def find_augmenting_path(start_edge):
        """Try to find augmenting path starting from start_edge"""
        path = [start_edge]
        visited_edges = {start_edge}
        u, v = edges[start_edge]
        # Try to match with u first
        for endpoint in [u, v]:
            if not used[endpoint]:
                return path, endpoint
        # Need to find augmenting path
        # BFS/DFS to find alternating path
        queue = [(start_edge, u)]  # (edge, endpoint to free)
        parent = {start_edge: (None, None)}
        target_free = None
        
        while queue and target_free is None:
            curr_edge, block_node = queue.pop(0)
            u, v = edges[curr_edge]
            other = v if block_node == u else u
            
            # Look at edges incident to 'other' that are matched
            for e in adj_idx[other]:
                if e == curr_edge or e in visited_edges:
                    continue
                if match[e] == -1:
                    continue
                eu, ev = edges[e]
                blocked = ev if eu == other else eu
                if not used[blocked]:
                    # Found augmenting path
                    target_free = blocked
                    parent[e] = (curr_edge, other)
                    path = []
                    curr = e
                    while curr is not None:
                        path.append(curr)
                        curr, _ = parent[curr]
                    return path[::-1], target_free
                else:
                    if e not in visited_edges:
                        visited_edges.add(e)
                        parent[e] = (curr_edge, other)
                        queue.append((e, blocked))
        return None, None
    
    # Greedy matching
    for e in range(m):
        if match[e] == -1:
            u, v = edges[e]
            # Try direct match
            if not used[u]:
                match[e] = u
                used[u] = True
            elif not used[v]:
                match[e] = v
                used[v] = True
            else:
                # Try augmenting
                path, free_node = find_augmenting_path(e)
                if path is None:
                    print("NO")
                    return
                # Augment along path
                # Unmatch edges at odd positions, match at even
                for i, pe in enumerate(path):
                    if i % 2 == 0:
                        pu, pv = edges[pe]
                        if not used[pu]:
                            match[pe] = pu
                            used[pu] = True
                        else:
                            match[pe] = pv
                            used[pv] = True
                    else:
                        old_match = match[pe]
                        used[old_match] = False
                        match[pe] = -1
    
    # Verify matching
    for e in range(m):
        if match[e] == -1:
            print("NO")
            return
    
    # Build contracted graph
    # Vertices are edges 0..m-1, two vertices are adjacent if they share a facility
    contracted_adj = [[] for _ in range(m)]
    for facility in range(1, n + 1):
        incident = adj_idx[facility]
        for i in range(len(incident)):
            for j in range(i + 1, len(incident)):
                e1, e2 = incident[i], incident[j]
                contracted_adj[e1].append(e2)
                contracted_adj[e2].append(e1)
    
    # 3-color the contracted graph
    color = [0] * m
    
    def dfs_color(u, c):
        color[u] = c
        for v in contracted_adj[u]:
            if color[v] == 0:
                if not dfs_color(v, 4 - c):
                    return False
            elif color[v] == c:
                return False
        return True
    
    for e in range(m):
        if color[e] == 0:
            if not dfs_color(e, 1):
                print("NO")
                return
    
    # Output
    print("YES")
    print(' '.join(map(str, color)))

solve()