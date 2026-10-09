from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    links = []
    graph = defaultdict(list)
    matched = {}
    
    idx = 2
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        links.append((a, b))
        graph[a].append(b)
        idx += 2
    
    # Try to find a perfect matching using Ford-Fulkerson-like approach
    # Actually, this is bipartite matching
    
    # Build the residual graph for Hopcroft-Karp or simpler augmenting paths
    pair_U = {}
    pair_V = {}
    U = list(range(1, q+1))
    V = list(range(q+1, 2*q+1))
    
    def bfs():
        queue = deque()
        dist = {}
        
        for u in U:
            if u not in pair_U:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[None] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[None]:
                for v in graph[u]:
                    if v in pair_V:
                        u_prime = pair_V[v]
                        if dist.get(u_prime, float('inf')) == float('inf'):
                            dist[u_prime] = dist[u] + 1
                            queue.append(u_prime)
                    else:
                        dist[None] = dist[u] + 1
        return dist[None] != float('inf')
    
    def dfs(u):
        for v in graph[u]:
            if v in pair_V:
                u_prime = pair_V[v]
                if dist.get(u_prime, -1) == dist[u] + 1 and dfs(u_prime):
                    pair_U[u] = v
                    pair_V[v] = u
                    return True
            else:
                pair_U[u] = v
                pair_V[v] = u
                return True
        dist[u] = float('inf')
        return False
    
    # Simplified version - use a greedy approach with backtracking for small cases
    # For large cases, implement proper bipartite matching
    
    # Greedy approach first
    used_ground = set()
    used_orbit = set()
    result = []
    
    # Sort links by ground array
    links_sorted = sorted(links)
    
    # Try greedy assignment
    for a, b in links_sorted:
        if a not in used_ground and b not in used_orbit:
            used_ground.add(a)
            used_orbit.add(b)
            result.append((a, b))
    
    if len(result) == q:
        print("YES")
        for a, b in result:
            print(a, b)
        return
    
    # Need proper matching algorithm
    # Reset and use a more thorough approach
    
    pair_U = {}
    pair_V = {}
    
    # Simple augmenting path approach
    def augment():
        visited = set()
        
        def dfs(u):
            if u in visited:
                return False
            visited.add(u)
            
            for v in graph[u]:
                if v not in pair_V:
                    pair_U[u] = v
                    pair_V[v] = u
                    return True
            
            for v in graph[u]:
                if v in pair_V:
                    u_prime = pair_V[v]
                    if dfs(u_prime):
                        pair_U[u] = v
                        pair_V[v] = u
                        return True
            return False
        
        for u in range(1, q+1):
            if u not in pair_U:
                visited.clear()
                if dfs(u):
                    return True
        return False
    
    # Run augmenting paths until no more improvements
    changed = True
    while changed:
        changed = augment()
    
    if len(pair_U) == q:
        print("YES")
        for u in range(1, q+1):
            if u in pair_U:
                print(u, pair_U[u])
    else:
        print("NO")

solve()