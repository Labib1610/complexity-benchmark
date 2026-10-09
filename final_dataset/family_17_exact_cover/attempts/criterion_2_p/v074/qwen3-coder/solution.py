from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for bipartite graph
    # Left side: 1 to q, Right side: q+1 to 2q
    adj = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
        edges.append((a, b))
    
    # Try to find a perfect matching in bipartite graph
    # Left part: 1..q, Right part: q+1..2q
    match_left = {}  # match_left[u] = v means u (left) is matched to v (right)
    match_right = {}  # match_right[v] = u means v (right) is matched to u (left)
    
    def bfs():
        # Find augmenting paths using BFS
        queue = deque()
        parent = {}
        visited = set()
        
        # Initialize queue with all unmatched left vertices
        for u in range(1, q + 1):
            if u not in match_left:
                queue.append(u)
                parent[u] = None
                visited.add(u)
        
        found_path = False
        sink = None
        
        while queue and not found_path:
            u = queue.popleft()
            
            # If u is a left vertex
            if u <= q:
                # Check all neighbors in right part
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
                            # Continue to the matched vertex in left part
                            next_u = match_right[v]
                            queue.append(next_u)
                            parent[next_u] = v
                            visited.add(next_u)
            else:
                # u is a right vertex
                # Continue to the matched vertex in left part
                if u in match_right:
                    next_u = match_right[u]
                    if next_u not in visited:
                        queue.append(next_u)
                        parent[next_u] = u
                        visited.add(next_u)
        
        if not found_path:
            return False
        
        # Augment along the path
        current = sink
        while parent[current] is not None:
            prev = parent[current]
            if current <= q:
                # This case shouldn't happen based on our algorithm
                pass
            else:
                # current is right vertex, prev is left vertex
                v = current
                u = prev
                if u in match_left:
                    old_v = match_left[u]
                    del match_right[old_v]
                match_left[u] = v
                match_right[v] = u
            current = prev
            
        return True
    
    # Keep finding augmenting paths until no more exist
    while bfs():
        pass
    
    # Check if we have a perfect matching
    if len(match_left) == q:
        print("YES")
        for u in range(1, q + 1):
            v = match_left[u]
            print(u, v)
    else:
        print("NO")

solve()