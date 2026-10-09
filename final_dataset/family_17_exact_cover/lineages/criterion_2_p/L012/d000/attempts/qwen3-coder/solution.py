from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    if t < q:
        print("NO")
        return
    
    # Build graph for bipartite matching
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using BFS-based algorithm (Hopcroft-Karp like approach)
    # But we'll use a simpler approach with DFS for this case
    
    match_controller = [0] * (q + 1)  # match_controller[c] = platform matched to controller c
    match_platform = [0] * (q + 1)    # match_platform[p-q] = controller matched to platform p
    
    def dfs(u, visited):
        for v in graph[u]:
            if visited[v - q]:
                continue
            visited[v - q] = True
            
            if match_platform[v - q] == 0 or dfs(match_platform[v - q], visited):
                match_controller[u] = v
                match_platform[v - q] = u
                return True
        return False
    
    matching = 0
    for i in range(1, q + 1):
        visited = [False] * (q + 1)
        if dfs(i, visited):
            matching += 1
    
    if matching < q:
        print("NO")
        return
    
    print("YES")
    for i in range(1, q + 1):
        print(i, match_controller[i])

solve()