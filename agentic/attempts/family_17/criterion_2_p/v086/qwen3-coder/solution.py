from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    if t < q:
        print("NO")
        return
    
    # Build adjacency list for bipartite graph
    # Left side: instrument bays (1 to q)
    # Right side: radiator panels (q+1 to 2*q)
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using BFS-based augmenting paths
    # This is essentially the Hopcroft-Karp algorithm simplified
    
    # mate[u] = v means u is matched to v
    mate_left = {}  # for instrument bays
    mate_right = {}  # for radiator panels
    
    def bfs():
        # Find shortest augmenting paths
        queue = deque()
        dist = {}
        
        for u in range(1, q + 1):
            if u not in mate_left:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        
        dist[None] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[None]:
                for v in graph[u]:
                    if v not in mate_right:
                        if dist[None] == float('inf'):
                            dist[None] = dist[u] + 1
                    else:
                        u_next = mate_right[v]
                        if dist[u_next] == float('inf'):
                            dist[u_next] = dist[u] + 1
                            queue.append(u_next)
        
        return dist[None] != float('inf')
    
    def dfs(u):
        if u is None:
            return True
            
        for v in graph[u]:
            if v not in mate_right:
                if dist[None] == dist[u] + 1:
                    mate_right[v] = u
                    mate_left[u] = v
                    return True
            else:
                u_next = mate_right[v]
                if dist[u_next] == dist[u] + 1:
                    if dfs(u_next):
                        mate_right[v] = u
                        mate_left[u] = v
                        return True
        
        dist[u] = float('inf')
        return False
    
    # Main matching loop
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if u not in mate_left:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, mate_left[u])
    else:
        print("NO")

solve()