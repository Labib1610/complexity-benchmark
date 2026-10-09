from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build graph for bipartite matching
    # Left side: 1 to q (primary tier)
    # Right side: 1 to q (representing q+1 to 2q, secondary tier)
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        b_shifted = b - q  # Convert to 1-based index in range 1 to q
        graph[a].append(b_shifted)
        edges.append((a, b_shifted))
    
    # Hopcroft-Karp algorithm for maximum bipartite matching
    def bfs():
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
                for v in graph[u]:
                    if dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[0] != float('inf')
    
    def dfs(u):
        if u != 0:
            for v in graph[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True
    
    # Initialize
    pair_u = [0] * (q + 1)  # pair_u[u] = v
    pair_v = [0] * (q + 1)  # pair_v[v] = u
    dist = [float('inf')] * (q + 1)
    
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, pair_u[u] + q)
    else:
        print("NO")

solve()