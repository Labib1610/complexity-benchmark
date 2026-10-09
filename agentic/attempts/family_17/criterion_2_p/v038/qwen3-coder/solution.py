from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for bipartite graph
    # Nodes 1 to q on left, q+1 to 2q on right
    adj = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
        edges.append((a, b))
    
    # Try to find a perfect matching in bipartite graph
    # Left side: 1 to q, Right side: q+1 to 2q
    
    match_left = {}  # match_left[u] = v means u (left) matched to v (right)
    match_right = {} # match_right[v] = u means v (right) matched to u (left)
    
    def bfs():
        # Find augmenting paths using BFS
        queue = deque()
        parent = {}
        visited = set()
        
        # Initialize with all unmatched left nodes
        for u in range(1, q + 1):
            if u not in match_left:
                queue.append(u)
                parent[u] = None
                visited.add(u)
        
        found_path = False
        sink = None
        
        while queue:
            u = queue.popleft()
            
            if u <= q:  # u is a left node
                # Explore neighbors (right nodes)
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        parent[v] = u
                        if v not in match_right:
                            # Found an augmenting path
                            found_path = True
                            sink = v
                            break
                        else:
                            # Continue to the matched node on left side
                            next_u = match_right[v]
                            queue.append(next_u)
                            parent[next_u] = v
                            visited.add(next_u)
            else:  # u is a right node
                # Explore the matched node on left (if exists)
                if u in match_right:
                    next_u = match_right[u]
                    if next_u not in visited:
                        visited.add(next_u)
                        parent[next_u] = u
                        queue.append(next_u)
        
            if found_path:
                break
        
        if not found_path:
            return False
        
        # Augment along the path
        current = sink
        while parent[current] is not None:
            prev = parent[current]
            if current <= q:  # current is left node
                match_left[current] = prev
                match_right[prev] = current
            else:  # current is right node
                match_right[current] = prev
                match_left[prev] = current
            current = prev
            
        return True
    
    # Keep finding augmenting paths until no more exist
    while bfs():
        pass
    
    # Check if we have a perfect matching
    if len(match_left) == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, match_left[u])
    else:
        print("NO")

solve()