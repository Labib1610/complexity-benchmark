from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    if t < q:
        print("NO")
        return
    
    # Build bipartite graph
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        # Convert to 0-indexed
        u = a - 1  # low-band station (0 to q-1)
        v = b - 1 - q  # high-band station (0 to q-1)
        graph[u].append(v)
        edges.append((u, v))
    
    # Try to find a perfect matching using Hopcroft-Karp algorithm approach
    # But we'll use a simpler approach with DFS for this case
    
    match_high = [-1] * q  # which low-band station is matched to each high-band
    match_low = [-1] * q   # which high-band station is matched to each low-band
    
    def dfs(u, visited):
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            
            # If high-band station v is unmatched or we can find augmenting path
            if match_high[v] == -1 or dfs(match_high[v], visited):
                match_high[v] = u
                match_low[u] = v
                return True
        return False
    
    matching = 0
    for u in range(q):
        visited = [False] * q
        if dfs(u, visited):
            matching += 1
    
    if matching < q:
        print("NO")
        return
    
    print("YES")
    for i in range(q):
        # Convert back to 1-indexed
        low_station = i + 1
        high_station = match_low[i] + 1 + q
        print(low_station, high_station)

solve()