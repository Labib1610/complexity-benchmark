from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for bipartite graph
    # Transmitters: 1 to q
    # Relays: q+1 to 2*q
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using BFS-based augmenting paths
    # This is essentially the Hopcroft-Karp algorithm simplified
    
    # match_relay[relay] = transmitter or -1
    # match_trans[transmitter] = relay or -1
    match_relay = {}
    match_trans = {}
    
    for r in range(q+1, 2*q+1):
        match_relay[r] = -1
    for t_id in range(1, q+1):
        match_trans[t_id] = -1
    
    def bfs():
        # Find shortest augmenting paths
        queue = deque()
        dist = {}
        
        for t_id in range(1, q+1):
            dist[t_id] = -1
            
        for t_id in range(1, q+1):
            if match_trans[t_id] == -1:
                dist[t_id] = 0
                queue.append(t_id)
        
        found = False
        while queue:
            u = queue.popleft()
            
            for v in graph[u]:
                matched_u = match_relay[v]
                if matched_u == -1:
                    found = True
                elif dist[matched_u] == -1:
                    dist[matched_u] = dist[u] + 1
                    queue.append(matched_u)
        
        return found
    
    def dfs(u):
        # Find augmenting path starting from u
        for v in graph[u]:
            matched_u = match_relay[v]
            if matched_u == -1:
                match_trans[u] = v
                match_relay[v] = u
                return True
            elif match_trans[matched_u] != -1 and \
                 (u not in dist or dist[matched_u] == dist[u] + 1):
                if dfs(matched_u):
                    match_trans[u] = v
                    match_relay[v] = u
                    return True
        if u in dist:
            dist[u] = -1  # Mark as visited
        return False
    
    # Main matching loop
    matching = 0
    while bfs():
        for t_id in range(1, q+1):
            if match_trans[t_id] == -1:
                if dfs(t_id):
                    matching += 1
    
    if matching == q:
        print("YES")
        for t_id in range(1, q+1):
            print(t_id, match_trans[t_id])
    else:
        print("NO")

solve()