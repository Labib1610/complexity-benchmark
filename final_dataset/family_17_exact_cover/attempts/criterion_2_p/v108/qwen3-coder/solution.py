from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build graph for bipartite matching
    # Surface modules: 1 to q
    # Orbital modules: q+1 to 2*q
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching
    # Use Hall's theorem approach with BFS-based augmenting paths
    
    match_orbital = {}  # orbital -> surface
    match_surface = {}  # surface -> orbital
    
    def bfs_match(start):
        """Find augmenting path starting from unmatched surface node"""
        queue = deque([start])
        parent = {start: None}
        visited = {start}
        
        while queue:
            node = queue.popleft()
            
            # If node is a surface module
            if node <= q:
                for orb in graph[node]:
                    if orb not in visited:
                        visited.add(orb)
                        if orb not in match_orbital:
                            # Found augmenting path
                            current = node
                            orb_node = orb
                            while current is not None:
                                prev_orb = match_surface.get(current)
                                match_surface[current] = orb_node
                                match_orbital[orb_node] = current
                                orb_node = prev_orb
                                current = parent[current]
                            return True
                        else:
                            next_surf = match_orbital[orb]
                            parent[next_surf] = node
                            queue.append(next_surf)
        
        return False
    
    # Find maximum matching
    matched = 0
    unmatched_surface = list(range(1, q + 1))
    
    updated = True
    while updated:
        updated = False
        for surf in unmatched_surface[:]:
            if surf not in match_surface:
                if bfs_match(surf):
                    matched += 1
                    unmatched_surface.remove(surf)
                    updated = True
    
    # Check if perfect matching exists
    if matched == q:
        print("YES")
        for surf in range(1, q + 1):
            print(surf, match_surface[surf])
    else:
        print("NO")

solve()