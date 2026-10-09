from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for bipartite graph
    # Left side: 1 to q (frequency references)
    # Right side: q+1 to 2q (phase trackers)
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using BFS-based augmenting paths (Hopcroft-Karp like)
    # But we'll use a simpler approach: try to find any maximum matching
    
    # match_right[b] = a means phase tracker b is matched to frequency reference a
    match_right = {}
    # match_left[a] = b means frequency reference a is matched to phase tracker b
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
                for b in graph[a]:
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
            
        for b in graph[a]:
            if b in match_right:
                aa = match_right[b]
                if dist[aa] == dist[a] + 1 and dfs(aa):
                    match_right[b] = a
                    match_left[a] = b
                    return True
            else:
                match_right[b] = a
                match_left[a] = b
                return True
        dist[a] = float('inf')
        return False
    
    # Main matching algorithm
    matching = 0
    dist = {}
    
    while bfs():
        for a in range(1, q + 1):
            if a not in match_left:
                if dfs(a):
                    matching += 1
    
    if matching == q:
        print("YES")
        for a in range(1, q + 1):
            print(a, match_left[a])
    else:
        print("NO")

solve()