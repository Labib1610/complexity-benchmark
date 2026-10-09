from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    if t < q:
        print("NO")
        return
    
    # Build adjacency list for bipartite graph
    # Left side: 1 to q, Right side: q+1 to 2q
    adj = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using BFS-based augmenting path algorithm
    # This is essentially the Hopcroft-Karp algorithm simplified for our needs
    
    # match_right[b] = a means asset b is matched to asset a
    match_right = {}
    match_left = {}
    
    def bfs():
        # Find shortest augmenting paths
        queue = deque()
        dist = {}
        
        for a in range(1, q + 1):
            if a not in match_left:
                dist[a] = 0
                queue.append(a)
            else:
                dist[a] = float('inf')
        dist[None] = float('inf')
        
        while queue:
            a = queue.popleft()
            if dist[a] < dist[None]:
                for b in adj[a]:
                    if b in match_right:
                        aa = match_right[b]
                        if dist[aa] == float('inf'):
                            dist[aa] = dist[a] + 1
                            queue.append(aa)
                    else:
                        dist[None] = dist[a] + 1
        return dist[None] != float('inf')
    
    def dfs(a):
        if a is None:
            return True
            
        for b in adj[a]:
            if b in match_right:
                aa = match_right[b]
                if dist.get(aa, float('inf')) == dist[a] + 1 and dfs(aa):
                    match_right[b] = a
                    match_left[a] = b
                    return True
            elif b not in match_right:
                match_right[b] = a
                match_left[a] = b
                return True
        dist[a] = float('inf')
        return False
    
    # Main matching loop
    matching = 0
    while bfs():
        for a in range(1, q + 1):
            if a not in match_left:
                if dfs(a):
                    matching += 1
    
    if matching < q:
        print("NO")
        return
    
    print("YES")
    for a in range(1, q + 1):
        b = match_left[a]
        print(a, b)

solve()