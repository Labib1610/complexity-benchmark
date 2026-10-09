from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for bipartite graph
    # Left side: 1 to q (reference oscillators)
    # Right side: q+1 to 2q (phase trackers)
    graph = defaultdict(list)
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    # Try to find a perfect matching using BFS (Hopcroft-Karp like approach)
    # But since we just need any maximum matching, we can use a simpler approach
    
    # matching[b] = a means oscillator b is matched to oscillator a
    # matched[a] = b means oscillator a is matched to oscillator b
    matching = {}
    matched = {}
    
    # Function to find augmenting path using BFS
    def bfs():
        # Find all unmatched vertices on left side
        queue = deque()
        parent = {}
        visited = set()
        
        for u in range(1, q + 1):
            if u not in matched:
                queue.append(u)
                parent[u] = None
                visited.add(u)
        
        while queue:
            u = queue.popleft()
            
            # If u is on left side (reference oscillator)
            if u <= q:
                # Check all neighbors
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        parent[v] = u
                        queue.append(v)
            else:
                # u is on right side (phase tracker)
                # Check if it's matched
                if u in matching:
                    # Continue to the matched vertex on left
                    partner = matching[u]
                    if partner not in visited:
                        visited.add(partner)
                        parent[partner] = u
                        queue.append(partner)
                else:
                    # Found an augmenting path to unmatched vertex on right
                    # Reconstruct path
                    path = []
                    current = u
                    while current is not None:
                        path.append(current)
                        current = parent[current]
                    path.reverse()
                    return path
        
        return None
    
    # Find maximum matching
    while True:
        path = bfs()
        if path is None:
            break
        
        # Augment along the path
        for i in range(0, len(path) - 1, 2):
            u, v = path[i], path[i + 1]
            matched[u] = v
            matching[v] = u
    
    # Check if we have a perfect matching
    if len(matched) == q:
        print("YES")
        for a in range(1, q + 1):
            b = matched[a]
            print(a, b)
    else:
        print("NO")

solve()