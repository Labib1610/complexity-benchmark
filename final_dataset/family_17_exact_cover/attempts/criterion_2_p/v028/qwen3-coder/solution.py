from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build graph for bipartite matching
    # Left side: flowers (1 to q)
    # Right side: moths (q+1 to 2*q)
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using Hopcroft-Karp algorithm approach
    # But we'll use a simpler approach with DFS-based augmenting paths
    
    match_flower = [0] * (q + 1)  # match_flower[f] = matched moth for flower f
    match_moth = [0] * (q + 1)    # match_moth[m] = matched flower for moth m (index relative to moth range)
    
    def dfs(u, visited):
        for v in graph[u]:
            v_idx = v - q  # Convert moth id to index 1..q
            if visited[v_idx]:
                continue
            visited[v_idx] = True
            
            # If moth v is unmatched or we can find augmenting path
            if match_moth[v_idx] == 0 or dfs(match_moth[v_idx], visited):
                match_flower[u] = v
                match_moth[v_idx] = u
                return True
        return False
    
    matching = 0
    for u in range(1, q + 1):
        visited = [False] * (q + 1)
        if dfs(u, visited):
            matching += 1
    
    if matching == q:
        print("YES")
        for i in range(1, q + 1):
            print(i, match_flower[i])
    else:
        print("NO")

solve()