from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build graph for bipartite matching
    # Left side: reactors 1 to q
    # Right side: fins q+1 to 2q
    # We'll use indices 1 to q for reactors and 1 to q for fins (fin i represents fin q+i)
    
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        fin_index = b - q  # Convert fin label to 1-based index
        graph[a].append(fin_index)
        edges.append((a, b))
    
    # Implement Hopcroft-Karp algorithm for maximum bipartite matching
    # But for simplicity, we'll use a simpler augmenting path approach
    
    # match[i] = j means reactor i is matched to fin j
    # match_rev[j] = i means fin j is matched to reactor i
    match = [0] * (q + 1)  # 1-indexed
    match_rev = [0] * (q + 1)  # 1-indexed
    
    def bfs():
        # BFS to find shortest augmenting paths
        dist = [0] * (q + 1)
        queue = deque()
        
        for u in range(1, q + 1):
            if match[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        
        dist[0] = float('inf')
        
        while queue:
            u = queue.popleft()
            
            if dist[u] < dist[0]:
                for v in graph[u]:
                    if dist[match_rev[v]] == float('inf'):
                        dist[match_rev[v]] = dist[u] + 1
                        queue.append(match_rev[v])
        
        return dist[0] != float('inf')
    
    def dfs(u):
        if u == 0:
            return True
            
        for v in graph[u]:
            if dist[match_rev[v]] == dist[u] + 1:
                if dfs(match_rev[v]):
                    match_rev[v] = u
                    match[u] = v
                    return True
        
        dist[u] = float('inf')
        return False
    
    # Hopcroft-Karp main algorithm
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if match[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching < q:
        print("NO")
        return
    
    print("YES")
    for u in range(1, q + 1):
        print(u, match[u] + q)

# Simpler implementation using a greedy approach with backtracking might be too slow
# Let's implement a standard augmenting path algorithm

def solve_simple():
    q, t = map(int, input().split())
    
    # Build adjacency list
    graph = defaultdict(list)
    edge_list = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
        edge_list.append((a, b))
    
    # Try to find a perfect matching
    # match_reactor[i] = j means reactor i is matched to fin j
    # match_fin[j] = i means fin j is matched to reactor i
    
    match_reactor = [0] * (q + 1)
    match_fin = [0] * (q + 1)
    
    def dfs(u, visited):
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            
            # If fin v is unmatched or we can find an augmenting path
            if match_fin[v] == 0 or dfs(match_fin[v], visited):
                match_reactor[u] = v
                match_fin[v] = u
                return True
        return False
    
    # Try to match each reactor
    matched = 0
    for u in range(1, q + 1):
        visited = [False] * (2 * q + 1)
        if dfs(u, visited):
            matched += 1
    
    if matched < q:
        print("NO")
        return
    
    print("YES")
    for u in range(1, q + 1):
        print(u, match_reactor[u])

solve_simple()