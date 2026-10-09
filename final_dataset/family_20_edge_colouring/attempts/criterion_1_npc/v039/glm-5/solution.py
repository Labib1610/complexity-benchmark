import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    # Check if graph is 3-regular
    for i in range(1, n + 1):
        if len(adj[i]) != 3:
            print("NO")
            return
    
    # Find a perfect matching using greedy augmentation
    matched = [False] * (n + 1)
    matching = [-1] * (n + 1)  # vertex -> edge index
    
    # Greedy pass
    for u in range(1, n + 1):
        if not matched[u]:
            for e_idx in adj[u]:
                v = edges[e_idx][0] + edges[e_idx][1] - u
                if not matched[v]:
                    matched[u] = True
                    matched[v] = True
                    matching[u] = e_idx
                    matching[v] = e_idx
                    break
    
    # Augmentation passes
    for _ in range(n):
        improved = False
        for u in range(1, n + 1):
            if matched[u]:
                continue
            # u is unmatched, try to find augmenting path
            # BFS from u through alternating edges
            parent = [-1] * (n + 1)  # parent vertex
            parent_edge = [-1] * (n + 1)  # edge used to reach vertex
            queue = [u]
            parent[u] = u  # mark as visited
            
            found = False
            head = 0
            while head < len(queue) and not found:
                curr = queue[head]
                head += 1
                
                if curr == u:
                    # From unmatched vertex, use non-matching edges
                    for e_idx in adj[curr]:
                        v = edges[e_idx][0] + edges[e_idx][1] - curr
                        if parent[v] == -1:
                            parent[v] = curr
                            parent_edge[v] = e_idx
                            queue.append(v)
                else:
                    # From matched vertex, use matching edge to go back
                    e_idx = matching[curr]
                    if e_idx == -1:
                        continue
                    v = edges[e_idx][0] + edges[e_idx][1] - curr
                    if parent[v] == -1:
                        parent[v] = curr
                        parent_edge[v] = e_idx
                        queue.append(v)
                        if not matched[v]:
                            # Found augmenting path to unmatched vertex
                            found = True
                            # Augment along path
                            tv = v
                            while tv != u:
                                p = parent[tv]
                                pe = parent_edge[tv]
                                # Update matching
                                if matching[p] != -1:
                                    old_edge = matching[p]
                                    op = edges[old_edge][0] + edges[old_edge][1] - p
                                    matching[op] = -1
                                    matched[op] = False
                                if matching[tv] != -1:
                                    old_edge = matching[tv]
                                    ot = edges[old_edge][0] + edges[old_edge][1] - tv
                                    matching[ot] = -1
                                    matched[ot] = False
                                matching[p] = pe
                                matching[tv] = pe
                                matched[p] = True
                                matched[tv] = True
                                tv = parent[p] if parent[p] != p else -1
                                if tv == -1:
                                    break
                            improved = True
                            break
            
            if improved:
                break
        
        if not improved:
            break
    
    # Check if perfect matching exists
    for i in range(1, n + 1):
        if not matched[i]:
            print("NO")
            return
    
    # Build the 2-regular graph (cycle decomposition)
    cycle_edges = [[] for _ in range(n + 1)]
    for v in range(1, n + 1):
        e_idx = matching[v]
        u = edges[e_idx][0] + edges[e_idx][1] - v
        cycle_edges[v].append((u, e_idx))
    
    # Assign colors: matching edges get color 1
    color = [0] * m
    for e_idx in range(m):
        u, v = edges[e_idx]
        if matching[u] == e_idx:
            color[e_idx] = 1
    
    # Find cycles and assign alternating colors 2 and 3
    visited = [False] * (n + 1)
    for start in range(1, n + 1):
        if visited[start]:
            continue
        
        # Find cycle starting from start
        cycle = []
        v = start
        while not visited[v]:
            visited[v] = True
            # Find next vertex in cycle (not using matching edge)
            for e_idx in adj[v]:
                if color[e_idx] == 0:
                    u = edges[e_idx][0] + edges[e_idx][1] - v
                    if not visited[u] or u == start:
                        cycle.append((v, u, e_idx))
                        v = u
                        break
            else:
                break
        
        if len(cycle) >= 2:
            # Assign alternating colors
            for i, (a, b, e_idx) in enumerate(cycle):
                color[e_idx] = 2 if i % 2 == 0 else 3
    
    # Verify the solution
    for v in range(1, n + 1):
        colors = set()
        for e_idx in adj[v]:
            colors.add(color[e_idx])
        if len(colors) != 3:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()