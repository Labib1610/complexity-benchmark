import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    
    batches = []
    for _ in range(k):
        s = int(next(iterator))
        t = int(next(iterator))
        d = int(next(iterator))
        batches.append((s, t, d))
        
    edges = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        cap = int(next(iterator))
        edges.append((u, v, cap))
        
    # Total nodes: 0 to n+k+1
    # 1 to n: original zones
    # n+1 to n+k: batch super sources
    # n+k+1: super sink
    S = n + k + 1
    T = n + k + 2
    total_nodes = n + k + 3
    
    head = [-1] * total_nodes
    to = []
    cap = []
    rev = []
    edge_cnt = 0
    
    def add_edge(u, v, c):
        nonlocal edge_cnt
        to.append(v)
        cap.append(c)
        rev.append(edge_cnt + 1)
        head.append(u)
        edge_cnt += 1
        
        to.append(u)
        cap.append(0)
        rev.append(edge_cnt - 1)
        head.append(v)
        edge_cnt += 1
        
    # Super source to batch sources
    total_demand = 0
    for i in range(k):
        s, t, d = batches[i]
        add_edge(S, n + 1 + i, d)
        total_demand += d
        
    # Batch sources to their induction zones
    for i in range(k):
        s, t, d = batches[i]
        add_edge(n + 1 + i, s, d)
        
    # Original edges
    for u, v, c in edges:
        add_edge(u, v, c)
        
    # Destination zones to super sink
    for i in range(k):
        s, t, d = batches[i]
        add_edge(t, T, d)
        
    # Dinic's algorithm
    level = [0] * total_nodes
    ptr = [0] * total_nodes
    
    def bfs():
        for i in range(total_nodes):
            level[i] = -1
        queue = [S]
        level[S] = 0
        head_q = 0
        while head_q < len(queue):
            u = queue[head_q]
            head_q += 1
            e = head[u]
            while e != -1:
                if cap[e] > 0 and level[to[e]] == -1:
                    level[to[e]] = level[u] + 1
                    queue.append(to[e])
                e = rev[e] if (e % 2 == 0) else -1
                if e == -1 and (e_rev := rev[e - 1] if e > 0 else -1) != -1:
                    pass # This logic is flawed, let's fix traversal
                
        # Corrected BFS traversal
        for i in range(total_nodes):
            level[i] = -1
        queue = [S]
        level[S] = 0
        head_q = 0
        while head_q < len(queue):
            u = queue[head_q]
            head_q += 1
            e = head[u]
            while e != -1:
                if cap[e] > 0 and level[to[e]] == -1:
                    level[to[e]] = level[u] + 1
                    queue.append(to[e])
                e = rev[e] if (e % 2 == 0) else -1
                if e == -1:
                    break
                # Wait, the adjacency list is stored in parallel arrays.
                # We need a next array for the adjacency list.
        # Let's properly maintain the `next` array for the adjacency list.
        pass

    # Let's rewrite the graph representation properly with a `nxt` array.
    head = [-1] * total_nodes
    to = []
    cap = []
    nxt = []
    rev_idx = []
    edge_cnt = 0
    
    def add_edge(u, v, c):
        nonlocal edge_cnt
        to.append(v); cap.append(c); nxt.append(head[u]); rev_idx.append(edge_cnt + 1); head[u] = edge_cnt; edge_cnt += 1
        to.append(u); cap.append(0); nxt.append(head[v]); rev_idx.append(edge_cnt - 1); head[v] = edge_cnt; edge_cnt += 1

    # Re-adding edges
    total_demand = 0
    for i in range(k):
        s, t, d = batches[i]
        add_edge(S, n + 1 + i, d)
        total_demand += d
        
    for i in range(k):
        s, t, d = batches[i]
        add_edge(n + 1 + i, s, d)
        
    for u, v, c in edges:
        add_edge(u, v, c)
        
    for i in range(k):
        s, t, d = batches[i]
        add_edge(t, T, d)
        
    level = [0] * total_nodes
    ptr = [0] * total_nodes
    
    def bfs():
        for i in range(total_nodes):
            level[i] = -1
        queue = [S]
        level[S] = 0
        head_q = 0
        while head_q < len(queue):
            u = queue[head_q]
            head_q += 1
            e = head[u]
            while e != -1:
                if cap[e] > 0 and level[to[e]] == -1:
                    level[to[e]] = level[u] + 1
                    queue.append(to[e])
                e = nxt[e]
        return level[T] != -1
        
    def dfs(u, pushed):
        if u == T:
            return pushed
        while ptr[u] != -1:
            e = ptr[u]
            if cap[e] > 0 and level[to[e]] == level[u] + 1:
                tr = dfs(to[e], min(pushed, cap[e]))
                if tr > 0:
                    cap[e] -= tr
                    cap[rev_idx[e]] += tr
                    return tr
            ptr[u] = nxt[e]
        return 0
        
    flow = 0
    while bfs():
        for i in range(total_nodes):
            ptr[i] = head[i]
        while True:
            pushed = dfs(S, float('inf'))
            if pushed == 0:
                break
            flow += pushed
            
    if flow != total_demand:
        print("NO")
        return
        
    print("YES")
    # The edges for batches are at indices 2*k + 2*i
    # Wait, the original edges are added after 2*k + 2*k = 4*k edges.
    # Batch i edges: 2*i (S to batch_i) and 2*k + 2*i (batch_i to s_i)
    # Wait, the order of add_edge is:
    # 0, 1: S to batch_0
    # 2, 3: S to batch_1
    # ...
    # 2k, 2k+1: batch_0 to s_0
    # 2k+2, 2k+3: batch_1 to s_1
    # ...
    # 4k, 4k+1: edge_0
    # 4k+2, 4k+3: edge_1
    # ...
    
    # For batch i, the edge from batch_i to s_i is at index 2*k + 2*i.
    # The flow on this edge is cap[2*k + 2*i + 1] (the reverse edge).
    
    # We need to find the flow of batch i on original edge j.
    # Original edge j is at index 4*k + 2*j.
    # We can just run k separate max flows to find the exact routing!
    # But wait, we can just find any valid decomposition.
    # Since the graph is a DAG for the batches (sources are n+1+i, sinks are t_i),
    # we can greedily extract paths.
    
    # Let's just run k max flows on the residual graph.
    # For each batch i, we push d_i flow from n+1+i to t_i.
    # Wait, the edges from S to n+1+i are already saturated.
    # We can just add infinite capacity from S to n+1+i, push d_i, then remove it.
    # Actually, the edges from n+1+i to s_i have residual capacity.
    # We can just find paths from n+1+i to t_i in the residual graph.
    
    # To avoid complex path extraction, we can just run Dinic for each batch!
    # Reset capacities, then for each batch, add its source and sink, run max flow, record flows, then update capacities.
    # This is O(k * E * sqrt(V)) which might be too slow if k is large.
    # k could be up to 100. E up to 1000. V up to 110. This is very fast!
    
    # Let's re-read the capacities.
    # We already modified `cap`. We can just restore it.
    # Actually, we can just copy the initial capacities.
    initial_cap = cap[:]
    
    # Reset cap to initial
    cap = initial_cap[:]
    
    ans = [[0] * m for _ in range(k)]
    
    for i in range(k):
        s, t, d = batches[i]
        # Add temporary source and sink for this batch
        # We can just use S and T for this batch!
        # But S and T are already connected to other batches.
        # We can just use n+1+i as source and t as sink.
        # Wait, the edges from S to n+1+i are already there.
        # We can just set cap[2*i] = d (S to batch_i)
        # And cap[4*k + 2*j] for original edges are already correct.
        # We just need to push flow from n+1+i to t.
        # Wait, the simplest way is to just find augmenting paths from n+1+i to t.
        
        # Let's just use a simple DFS to find paths for batch i
        visited = [False] * total_nodes
        
        def dfs_path(u, pushed):
            if u == t:
                return pushed
            visited[u] = True
            e = head[u]
            while e != -1:
                if cap[e] > 0 and not visited[to[e]]:
                    tr = dfs_path(to[e], min(pushed, cap[e]))
                    if tr > 0:
                        cap[e] -= tr
                        cap[rev_idx[e]] += tr
                        # If this edge is an original edge, record it
                        # Original edges are from 4*k to 4*k + 2*m - 1
                        if 4 * k <= e < 4 * k + 2 * m and e % 2 == 0:
                            ans[i][e // 2 - 2 * k] += tr
                        elif 4 * k <= rev_idx[e] < 4 * k + 2 * m and rev_idx[e] % 2 == 0:
                            # This means we are pushing flow back on an original edge
                            ans[i][rev_idx[e] // 2 - 2 * k] -= tr
                        return tr
                e = nxt[e]
            return 0

        pushed_flow = 0
        while pushed_flow < d:
            visited = [False] * total_nodes
            tr = dfs_path(n + 1 + i, d - pushed_flow)
            if tr == 0:
                break
            pushed_flow += tr
            
    for i in range(k):
        print(" ".join(map(str, ans[i])))

if __name__ == '__main__':
    solve()