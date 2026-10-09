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
    
    # Implement Hopcroft-Karp algorithm for maximum matching
    def bfs():
        queue = deque()
        for u in range(q):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[-1] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[-1]:
                for v in graph[u]:
                    if dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[-1] != float('inf')
    
    def dfs(u):
        if u != -1:
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
    pair_u = [-1] * q  # pair_u[u] = v if u is matched to v, -1 otherwise
    pair_v = [-1] * q  # pair_v[v] = u if v is matched to u, -1 otherwise
    dist = [float('inf')] * (q + 1)  # Distance array, last element is NIL
    
    matching = 0
    while bfs():
        for u in range(q):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    
    if matching == q:
        print("YES")
        for u in range(q):
            # Convert back to 1-indexed
            print(u + 1, pair_u[u] + q + 1)
    else:
        print("NO")

solve()