from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    if t < q:
        print("NO")
        return
    
    # Build graph for bipartite matching
    # Left side: modules 1 to q
    # Right side: ports q+1 to 2q
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching
    # Using Hopcroft-Karp algorithm implementation
    
    # match_right[b] = a if port b is matched to module a, 0 otherwise
    match_right = [0] * (2*q + 1)
    # match_left[a] = b if module a is matched to port b, 0 otherwise
    match_left = [0] * (q + 1)
    
    def bfs():
        dist = [0] * (q + 1)
        queue = deque()
        
        for u in range(1, q + 1):
            if match_left[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        
        dist[0] = float('inf')
        
        while queue:
            u = queue.popleft()
            
            if dist[u] < dist[0]:
                for v in graph[u]:
                    if dist[match_right[v]] == float('inf'):
                        dist[match_right[v]] = dist[u] + 1
                        queue.append(match_right[v])
        
        return dist[0] != float('inf')
    
    def dfs(u):
        if u == 0:
            return True
            
        for v in graph[u]:
            if dist[match_right[v]] == dist[u] + 1:
                if dfs(match_right[v]):
                    match_right[v] = u
                    match_left[u] = v
                    return True
        
        dist[u] = float('inf')
        return False
    
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if match_left[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, match_left[u])
    else:
        print("NO")

solve()