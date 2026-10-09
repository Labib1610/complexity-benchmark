from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build bipartite graph
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        # Convert to 0-indexed
        graph[a-1].append(b-q-1)
        graph[b-q-1].append(a-1)
        edges.append((a-1, b-q-1))
    
    # Hungarian algorithm / Max flow to find maximum matching
    # We'll use Hopcroft-Karp implementation
    
    def bfs():
        queue = deque()
        for u in range(q):
            if match_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[-1] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[-1]:
                for v in graph[u]:
                    if dist[match_v[v]] == float('inf'):
                        dist[match_v[v]] = dist[u] + 1
                        queue.append(match_v[v])
        return dist[-1] != float('inf')
    
    def dfs(u):
        if u != -1:
            for v in graph[u]:
                if dist[match_v[v]] == dist[u] + 1:
                    if dfs(match_v[v]):
                        match_v[v] = u
                        match_u[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True
    
    # Initialize
    match_u = [-1] * q  # match for vertices 0 to q-1 (acidic)
    match_v = [-1] * q  # match for vertices 0 to q-1 (alkaline, shifted)
    dist = [float('inf')] * (q + 1)  # distance array, last element is NIL
    
    matching = 0
    while bfs():
        for u in range(q):
            if match_u[u] == -1 and dfs(u):
                matching += 1
    
    if matching != q:
        print("NO")
        return
    
    print("YES")
    for i in range(q):
        # Convert back to 1-indexed
        print(i + 1, match_u[i] + q + 1)

solve()