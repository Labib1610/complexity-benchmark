from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    if t < q:
        print("NO")
        return
    
    # Build adjacency list for the bipartite graph
    adj = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using BFS-based augmenting paths
    # This is essentially the Hopcroft-Karp algorithm simplified
    
    # match_vocalist[v] = matched instrumentalist for vocalist v
    match_vocalist = [0] * (q + 1)
    # match_instrumentalist[i] = matched vocalist for instrumentalist i
    match_instrumentalist = [0] * (2 * q + 1)
    
    def bfs():
        dist = [0] * (q + 1)
        queue = deque()
        
        for v in range(1, q + 1):
            if match_vocalist[v] == 0:
                dist[v] = 0
                queue.append(v)
            else:
                dist[v] = float('inf')
        
        dist[0] = float('inf')
        
        while queue:
            v = queue.popleft()
            
            if dist[v] < dist[0]:
                for i in adj[v]:
                    # i is an instrumentalist
                    next_v = match_instrumentalist[i]
                    if dist[next_v] == 0:  # next_v is 0 or not visited
                        dist[next_v] = dist[v] + 1
                        if next_v != 0:
                            queue.append(next_v)
        
        return dist[0] != float('inf')
    
    def dfs(v):
        if v == 0:
            return True
            
        for i in adj[v]:
            next_v = match_instrumentalist[i]
            if dist[next_v] == dist[v] + 1 and dfs(next_v):
                match_vocalist[v] = i
                match_instrumentalist[i] = v
                return True
                
        dist[v] = float('inf')
        return False
    
    matching = 0
    while bfs():
        for v in range(1, q + 1):
            if match_vocalist[v] == 0 and dfs(v):
                matching += 1
    
    if matching == q:
        print("YES")
        for v in range(1, q + 1):
            print(v, match_vocalist[v])
    else:
        print("NO")

solve()