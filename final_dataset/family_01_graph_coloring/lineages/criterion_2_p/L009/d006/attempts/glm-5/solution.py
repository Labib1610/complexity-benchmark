import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    deg = [0] * n
    edges = []
    
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1
        edges.append((u, v))
    
    color = [-1] * n
    is_bipartite = True
    
    for i in range(n):
        if color[i] == -1:
            stack = [i]
            color[i] = 0
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
    
    if is_bipartite:
        s = [1] * n
        for i in range(n):
            if color[i] == 1:
                s[i] = 2
        print("YES")
        print(' '.join(map(str, s)))
        return
    
    # Graph is not bipartite, try s[i] = 2 for all
    # Check if sum(deg[i] * 4) - sum(2 * 2 * 2) = m
    # sum(deg[i] * 4) = 8m, sum(8) = 8m, so 8m - 8m = 0 != m (unless m=0)
    # So we need to find a vertex cover
    # Try to find a vertex cover using greedy approach
    
    # We'll use a greedy approach: repeatedly pick the vertex with highest degree
    # and mark it as covered (remove it and its edges)
    
    # Use adjacency list with sets for efficient removal
    adj_sets = [set(neighbors) for neighbors in adj]
    deg_current = deg[:]
    
    # Priority queue: (-degree, vertex)
    import heapq
    heap = [(-deg_current[i], i) for i in range(n)]
    heapq.heapify(heap)
    
    in_cover = [False] * n
    covered_edges = 0
    
    while covered_edges < m:
        # Find vertex with maximum degree
        while heap:
            neg_deg, u = heapq.heappop(heap)
            if not in_cover[u] and deg_current[u] == -neg_deg:
                break
        else:
            break  # No more vertices
        
        in_cover[u] = True
        # Remove all edges incident to u
        for v in adj[u]:
            if not in_cover[v] and u in adj_sets[v]:
                adj_sets[v].discard(u)
                deg_current[v] -= 1
                heapq.heappush(heap, (-deg_current[v], v))
                covered_edges += 1
    
    if covered_edges < m:
        print("NO")
        return
    
    s = [1] * n
    for i in range(n):
        if in_cover[i]:
            s[i] = 2
    
    print("YES")
    print(' '.join(map(str, s)))

solve()