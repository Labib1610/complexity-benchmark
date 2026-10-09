from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for bipartite graph
    # Vocalists: 1 to q
    # Instrumentalists: q+1 to 2q
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
    
    # Check if we have a perfect matching using Hall's theorem approach
    # But we'll use a more direct approach: try to find maximum matching
    
    # Use Hopcroft-Karp or simplified Ford-Fulkerson for bipartite matching
    # Let's implement a BFS-based approach to find maximum matching
    
    match_vocalist = [-1] * (q + 1)      # match_vocalist[v] = matched instrumentalist
    match_instrumentalist = [-1] * (2 * q + 1)  # match_instrumentalist[i] = matched vocalist
    
    def bfs():
        dist = [-1] * (q + 1)
        queue = deque()
        
        # Initialize distances for free vertices
        for v in range(1, q + 1):
            if match_vocalist[v] == -1:
                dist[v] = 0
                queue.append(v)
            else:
                dist[v] = -1
        
        found = False
        while queue:
            v = queue.popleft()
            
            if dist[v] < float('inf'):
                for u in adj[v]:
                    if match_instrumentalist[u] == -1:
                        # Found an augmenting path
                        found = True
                    elif dist[match_instrumentalist[u]] == -1:
                        dist[match_instrumentalist[u]] = dist[v] + 1
                        queue.append(match_instrumentalist[u])
        return found
    
    def dfs(v):
        for u in adj[v]:
            if match_instrumentalist[u] == -1:
                # Augmenting path found
                match_instrumentalist[u] = v
                match_vocalist[v] = u
                return True
            elif match_instrumentalist[u] != -1:
                paired_v = match_instrumentalist[u]
                if dist[paired_v] == dist[v] + 1:
                    if dfs(paired_v):
                        match_instrumentalist[u] = v
                        match_vocalist[v] = u
                        return True
        dist[v] = float('inf')
        return False
    
    # Main matching loop
    matching = 0
    while bfs():
        for v in range(1, q + 1):
            if match_vocalist[v] == -1:
                if dfs(v):
                    matching += 1
    
    if matching == q:
        print("YES")
        for v in range(1, q + 1):
            print(v, match_vocalist[v])
    else:
        print("NO")

solve()