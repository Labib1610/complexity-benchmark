import sys
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    index = 2
    edges = []
    adj = defaultdict(list)
    
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        edges.append((a, b))
        adj[a].append(b)
        index += 2
    
    # Build the bipartite graph for maximum matching
    # Controllers: 1 to q
    # Platforms: q+1 to 2*q
    
    # We'll use Hopcroft-Karp algorithm implementation for maximum bipartite matching
    
    match_controller = [0] * (q + 1)  # match_controller[c] = matched platform
    match_platform = [0] * (q + 1)    # match_platform[p - q] = matched controller
    
    # Build adjacency list for controllers to platforms (0-indexed for platforms)
    controller_adj = [[] for _ in range(q + 1)]
    for a, b in edges:
        controller_adj[a].append(b - q)  # Convert platform id to 1-based index 1..q
        
    def bfs():
        dist = [-1] * (q + 1)
        queue = deque()
        for c in range(1, q + 1):
            if match_controller[c] == 0:
                dist[c] = 0
                queue.append(c)
        
        found = False
        while queue:
            c = queue.popleft()
            for p_idx in controller_adj[c]:
                p = p_idx  # p is 1-based index
                matched_c = match_platform[p]
                if matched_c == 0:
                    found = True
                elif dist[matched_c] == -1:
                    dist[matched_c] = dist[c] + 1
                    queue.append(matched_c)
        return found
    
    def dfs(c):
        for p_idx in controller_adj[c]:
            p = p_idx
            matched_c = match_platform[p]
            if matched_c == 0:
                match_platform[p] = c
                match_controller[c] = p
                return True
            elif match_controller[matched_c] == p and dist[matched_c] == dist[c] + 1:
                if dfs(matched_c):
                    match_platform[p] = c
                    match_controller[c] = p
                    return True
        dist[c] = -1
        return False
    
    # Hopcroft-Karp main loop
    matching = 0
    while True:
        found = bfs()
        if not found:
            break
        for c in range(1, q + 1):
            if match_controller[c] == 0:
                if dfs(c):
                    matching += 1
    
    if matching == q:
        print("YES")
        for c in range(1, q + 1):
            print(c, match_controller[c] + q)
    else:
        print("NO")

solve()