from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for the bipartite graph
    # Vocalists: 1 to q
    # Instrumentalists: q+1 to 2q
    adj = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
        edges.append((a, b))
    
    # Try to find a perfect matching using BFS-based augmenting paths (Hopcroft-Karp like)
    # But we'll use a simpler approach: try to find any maximum matching
    
    # match_vocalist[v] = matched instrumentalist for vocalist v (or -1 if unmatched)
    # match_instrumentalist[i] = matched vocalist for instrumentalist i (or -1 if unmatched)
    match_vocalist = [-1] * (q + 1)  # 1-indexed
    match_instrumentalist = [-1] * (2*q + 1)  # 1-indexed
    
    def bfs():
        # Find shortest augmenting paths
        dist = [-1] * (q + 1)
        queue = deque()
        
        # Initialize: put all unmatched vocalists in queue
        for v in range(1, q + 1):
            if match_vocalist[v] == -1:
                dist[v] = 0
                queue.append(v)
            else:
                dist[v] = -1
        
        found = False
        while queue:
            v = queue.popleft()
            
            if dist[v] < (dist[0] if found else float('inf')):
                for i in adj[v]:
                    # If instrumentalist i is not matched to anyone or ...
                    next_v = match_instrumentalist[i]
                    if next_v == -1:
                        found = True
                    elif dist[next_v] == -1:
                        dist[next_v] = dist[v] + 1
                        queue.append(next_v)
        
        return found
    
    def dfs(v):
        for i in adj[v]:
            next_v = match_instrumentalist[i]
            if next_v == -1 or (dist[next_v] == dist[v] + 1 and dfs(next_v)):
                match_vocalist[v] = i
                match_instrumentalist[i] = v
                return True
        dist[v] = -1  # Mark as visited
        return False
    
    # Main matching algorithm
    matching = 0
    while bfs():
        for v in range(1, q + 1):
            if match_vocalist[v] == -1:
                if dfs(v):
                    matching += 1
    
    if matching == q:
        print("YES")
        for v in range(1, q + 1):
            print(v, match_vocalist[v])
    else:
        print("NO")

solve()