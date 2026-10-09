from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build bipartite graph
    # Left side: vocalists 1 to q
    # Right side: instrumentalists q+1 to 2q
    graph = defaultdict(list)
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    # Try to find a perfect matching using Hopcroft-Karp algorithm approach
    # But we'll use a simpler approach with DFS matching
    
    match_vocalist = [0] * (q + 1)  # match_vocalist[v] = matched instrumentalist for vocalist v
    match_instrumentalist = [0] * (q + 1)  # match_instrumentalist[i] = matched vocalist for instrumentalist (i+q)
    
    def dfs(v, visited):
        for u in graph[v]:
            inst_id = u - q  # Convert to 1-based index in instrumentalist array
            if visited[inst_id]:
                continue
            visited[inst_id] = True
            
            # If instrumentalist u is unmatched or we can find augmenting path
            if match_instrumentalist[inst_id] == 0 or dfs(match_instrumentalist[inst_id], visited):
                match_vocalist[v] = u
                match_instrumentalist[inst_id] = v
                return True
        return False
    
    matching = 0
    for v in range(1, q + 1):
        visited = [False] * (q + 1)
        if dfs(v, visited):
            matching += 1
    
    if matching == q:
        print("YES")
        for v in range(1, q + 1):
            print(v, match_vocalist[v])
    else:
        print("NO")

solve()