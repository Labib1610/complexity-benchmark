from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Create adjacency list for bipartite graph
    # Extractors: 1 to q
    # Vents: q+1 to 2*q
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using Ford-Fulkerson with BFS (Edmonds-Karp)
    # This is a bipartite matching problem
    
    # match_vent[v] = e means vent v is matched to extractor e
    match_vent = {}
    match_extractor = {}
    
    def bfs():
        # Find augmenting path
        queue = deque()
        parent = {}
        visited = set()
        
        # Start with all unmatched extractors
        for e in range(1, q + 1):
            if e not in match_extractor:
                queue.append(e)
                parent[e] = None
                visited.add(e)
        
        found_path = False
        sink = None
        
        while queue:
            node = queue.popleft()
            
            # If node is an extractor
            if node <= q:
                # Visit all neighbors (vents)
                for vent in graph[node]:
                    if vent not in visited:
                        visited.add(vent)
                        parent[vent] = node
                        # If vent is unmatched, we found an augmenting path
                        if vent not in match_vent:
                            found_path = True
                            sink = vent
                            break
                        else:
                            # Continue to the matched extractor
                            next_extractor = match_vent[vent]
                            queue.append(next_extractor)
                            parent[next_extractor] = vent
                            visited.add(next_extractor)
            
            if found_path:
                break
        
        if not found_path:
            return False
        
        # Update matching along the path
        current = sink
        while parent[current] is not None:
            prev = parent[current]
            if current <= q:  # current is extractor
                match_extractor[prev] = current
                match_vent[current] = prev
            else:  # current is vent
                match_extractor[current] = prev
                match_vent[prev] = current
            current = parent[prev]
        
        return True
    
    # Keep finding augmenting paths until no more exist
    while bfs():
        pass
    
    # Check if we have a perfect matching
    if len(match_extractor) == q:
        print("YES")
        for e in range(1, q + 1):
            print(e, match_extractor[e])
    else:
        print("NO")

solve()