from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Create adjacency list for bipartite graph
    # Left side: panels 1 to q (sun-facing)
    # Right side: panels q+1 to 2q (deep-space-facing)
    adj = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
        edges.append((a, b))
    
    # Try to find a maximum matching using BFS (Hopcroft-Karp like approach)
    # But we can use a simpler approach: try to find augmenting paths
    
    # match_right[b] = a means panel b is matched to panel a
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
                        return True
        return False
    
    def dfs(a):
        if a is None:
            return True
        for b in adj[a]:
            if b in match_right:
                aa = match_right[b]
                if dist[aa] == dist[a] + 1 and dfs(aa):
                    match_right[b] = a
                    match_left[a] = b
                    return True
            elif dist[None] == dist[a] + 1 and dfs(None):
                match_right[b] = a
                match_left[a] = b
                return True
        dist[a] = float('inf')
        return False
    
    # Main matching algorithm
    while bfs():
        for a in range(1, q + 1):
            if a not in match_left:
                dfs(a)
    
    # Check if we have a perfect matching
    if len(match_left) == q:
        print("YES")
        for a in range(1, q + 1):
            print(a, match_left[a])
    else:
        print("NO")

solve()