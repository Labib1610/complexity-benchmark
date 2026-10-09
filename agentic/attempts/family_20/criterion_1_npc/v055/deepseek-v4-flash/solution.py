import sys
sys.setrecursionlimit(10000)

def solve():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # For matching
    matched = [-1] * n
    edge_used = [False] * m
    active = [True] * n
    deg = [len(adj[i]) for i in range(n)]
    
    # We'll use a list to record operations for undo
    # But we can just implement match/unmatch functions that modify state and we can reverse.
    
    def get_min_vertex():
        best = -1
        best_deg = 4
        for v in range(n):
            if active[v]:
                d = deg[v]
                if d == 0:
                    return v  # will cause failure
                if d < best_deg:
                    best_deg = d
                    best = v
                    if d == 1:
                        break
        return best
    
    def match(v, u, e):
        # match v and u
        matched[v] = u
        matched[u] = v
        edge_used[e] = True
        active[v] = False
        active[u] = False
        # update degrees of neighbors
        for w, ei in adj[v]:
            if active[w]:
                deg[w] -= 1
        for w, ei in adj[u]:
            if active[w]:
                deg[w] -= 1
    
    def unmatch(v, u, e):
        # undo match
        matched[v] = -1
        matched[u] = -1
        edge_used[e] = False
        active[v] = True
        active[u] = True
        for w, ei in adj[v]:
            if active[w]:
                deg[w] += 1
        for w, ei in adj[u]:
            if active[w]:
                deg[w] += 1
    
    def search():
        v = get_min_vertex()
        if v == -1:
            return True
        if deg[v] == 0:
            return False
        if deg[v] == 1:
            # force match with its only active neighbor
            for u, e in adj[v]:
                if active[u]:
                    break
            # match
            match(v, u, e)
            if search():
                return True
            unmatch(v, u, e)
            return False
        else:
            # try each neighbor
            # shuffle to avoid worst-case? We'll just iterate in order.
            for u, e in adj[v]:
                if active[u]:
                    match(v, u, e)
                if search():
                    return True
                unmatch(v, u, e)
            return False
    
    if not search():
        print("NO")
        return
    
    # Found perfect matching.
    color = [0] * m
    for i in range(m):
        if edge_used[i]:
            color[i] = 1
    
    # Build remaining graph
    rem_adj = [[] for _ in range(n)]
    for i in range(m):
        if not edge_used[i]:
            u, v = edges[i]
            rem_adj[u].append((v, i))
            rem_adj[v].append((u, i))
    
    # Color cycles
    visited = [False] * n
    for start in range(n):
        if not visited[start]:
            continue
        # start a cycle
        visited[start] = True
        # pick first neighbor
        if not rem_adj[start]:
            continue  # isolated? shouldn't happen
        prev = -1
        cur = start
        # We'll traverse the cycle
        # We need to assign colors to edges
        # We'll start with the first edge from start
        # We'll traverse until we return to start
        # We'll use a while loop
        # We'll keep track of the edge we came from to avoid going back
        # We'll assign color 2 to the first edge, then 3, etc.
        # We'll mark vertices visited as we go.
        # We'll need to know which edge to take next.
        # We'll start at start, take its first neighbor.
        # We'll assign color 2 to that edge.
        # Then move to that neighbor, and from there, take the other edge (not the one we came from).
        # Continue until we return to start.
        # We'll use a variable 'color_to_assign' alternating 2,3.
        # We'll also mark the edge as colored.
        # We'll need to know the edge index.
        # Let's implement.
        # We'll use a stack? Actually, we can just follow.
        # We'll set cur = start, prev_edge = -1, next_color = 2
        # While True:
        #   find the next neighbor from cur that is not the one we came from (if prev_edge != -1)
        #   if we are at start and have already taken one edge, we need to stop when we come back.
        # We'll use a visited_edges set? But we can just stop when we return to start and have taken at least one edge.
        # Let's do:
        cur = start
        prev_edge = -1
        next_color = 2
        while True:
            # find next edge
            for nxt, ei in rem_adj[cur]:
                if ei != prev_edge:
                    break
            # assign color
            color[ei] = next_color
            # mark the neighbor as visited
            visited[nxt] = True
            # move
            prev_edge = ei
            cur = nxt
            next_color = 5 - next_color  # switch 2<->3
            if cur == start:
                break
    # Output
    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()