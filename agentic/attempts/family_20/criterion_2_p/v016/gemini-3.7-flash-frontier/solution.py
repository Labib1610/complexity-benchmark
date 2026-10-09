import sys

# Increase recursion depth for deep recursive calls and Euler tours
sys.setrecursionlimit(2000000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    S = int(input_data[0])
    T = int(input_data[1])
    m = int(input_data[2])
    
    if m == 0:
        print("YES")
        print()
        return

    edges = []
    deg_L = [0] * (S + 1)
    deg_R = [0] * (T + 1)
    
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        edges.append((u - 1, v - 1, i))
        deg_L[u - 1] += 1
        deg_R[v - 1] += 1
        
    D = max(max(deg_L), max(deg_R))
    if D == 0:
        print("YES")
        print()
        return

    # Balance number of vertices in L and R
    N = max(S, T)
    
    # Pad degrees to size N
    deg_u = [0] * N
    deg_v = [0] * N
    for u, v, _ in edges:
        deg_u[u] += 1
        deg_v[v] += 1
        
    # Add dummy edges to make it D-regular
    dummy_edges = []
    dummy_id = m
    u_idx = 0
    v_idx = 0
    while u_idx < N and v_idx < N:
        while u_idx < N and deg_u[u_idx] == D:
            u_idx += 1
        while v_idx < N and deg_v[v_idx] == D:
            v_idx += 1
        if u_idx < N and v_idx < N:
            add = min(D - deg_u[u_idx], D - deg_v[v_idx])
            for _ in range(add):
                dummy_edges.append((u_idx, v_idx, dummy_id))
                dummy_id += 1
            deg_u[u_idx] += add
            deg_v[v_idx] += add

    all_edges = edges + dummy_edges
    ans = [0] * m

    # Hopcroft-Karp for finding a 1-factor in d-regular bipartite graph
    def find_perfect_matching(n_verts, cur_edges):
        adj = [[] for _ in range(n_verts)]
        for u, v, eid in cur_edges:
            adj[u].append((v, eid))
            
        pair_u = [-1] * n_verts
        pair_v = [-1] * n_verts
        dist = [-1] * n_verts
        
        from collections import deque
        
        def bfs():
            q = deque()
            for u in range(n_verts):
                if pair_u[u] == -1:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = -1
            found = False
            while q:
                u = q.popleft()
                for v, eid in adj[u]:
                    p_u = pair_v[v]
                    if p_u != -1:
                        if dist[p_u] == -1:
                            dist[p_u] = dist[u] + 1
                            q.append(p_u)
                    else:
                        found = True
            return found

        ptr = [0] * n_verts
        def dfs(u):
            for i in range(ptr[u], len(adj[u])):
                ptr[u] = i + 1
                v, eid = adj[u][i]
                p_u = pair_v[v]
                if p_u == -1 or (dist[p_u] == dist[u] + 1 and dfs(p_u)):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
            return False

        matching_size = 0
        while bfs():
            for i in range(n_verts):
                ptr[i] = 0
            for u in range(n_verts):
                if pair_u[u] == -1:
                    if dfs(u):
                        matching_size += 1
                        
        # Extract matching edges and remaining edges
        match_edges = []
        rem_edges = []
        
        # We need to map the matched (u, v) back to an edge id
        matched_edge_for_u = {}
        # Since multigraph can exist, mark used edge
        used_v = [False] * n_verts
        v_matched_to = {v: pair_v[v] for v in range(n_verts) if pair_v[v] != -1}
        
        u_matched_edge = [-1] * n_verts
        for u, v, eid in cur_edges:
            if v_matched_to.get(v) == u and u_matched_edge[u] == -1:
                u_matched_edge[u] = eid
                match_edges.append((u, v, eid))
                # remove from v_matched_to so parallel edges don't double match
                v_matched_to[v] = -2
            else:
                rem_edges.append((u, v, eid))
                
        return match_edges, rem_edges

    # Euler tour decomposition for even degree regular bipartite graph
    def split_even(n_verts, cur_edges):
        adj = [[] for _ in range(2 * n_verts)]
        num_e = len(cur_edges)
        used = [False] * num_e
        
        for idx, (u, v, eid) in enumerate(cur_edges):
            # L is 0..n_verts-1, R is n_verts..2*n_verts-1
            vr = v + n_verts
            adj[u].append((vr, idx))
            adj[vr].append((u, idx))
            
        group1 = []
        group2 = []
        
        pos = [0] * (2 * n_verts)
        for start_node in range(2 * n_verts):
            if pos[start_node] < len(adj[start_node]):
                stack = [start_node]
                edge_stack = []
                while stack:
                    curr = stack[-1]
                    while pos[curr] < len(adj[curr]) and used[adj[curr][pos[curr]][1]]:
                        pos[curr] += 1
                    if pos[curr] < len(adj[curr]):
                        nxt, e_idx = adj[curr][pos[curr]]
                        pos[curr] += 1
                        used[e_idx] = True
                        stack.append(nxt)
                        edge_stack.append(e_idx)
                    else:
                        stack.pop()
                        if edge_stack:
                            # Euler tour path segment
                            pass
                # The iterative Hierholzer can build the cycle
        
        # Alternatively, a simple cycle traversal
        pos = [0] * (2 * n_verts)
        used = [False] * num_e
        for i in range(2 * n_verts):
            while pos[i] < len(adj[i]):
                while pos[i] < len(adj[i]) and used[adj[i][pos[i]][1]]:
                    pos[i] += 1
                if pos[i] >= len(adj[i]):
                    break
                
                # Start a circuit
                curr = i
                cycle_edges = []
                while True:
                    while pos[curr] < len(adj[curr]) and used[adj[curr][pos[curr]][1]]:
                        pos[curr] += 1
                    if pos[curr] >= len(adj[curr]):
                        break
                    nxt, e_idx = adj[curr][pos[curr]]
                    pos[curr] += 1
                    used[e_idx] = True
                    cycle_edges.append(e_idx)
                    curr = nxt
                    if curr == i:
                        break
                
                for k, e_idx in enumerate(cycle_edges):
                    if k % 2 == 0:
                        group1.append(cur_edges[e_idx])
                    else:
                        group2.append(cur_edges[e_idx])
                        
        return group1, group2

    def color_graph(cur_edges, d, color_offset):
        if d == 0 or not cur_edges:
            return
        if d == 1:
            for u, v, eid in cur_edges:
                if eid < m:
                    ans[eid] = color_offset
            return
        
        if d % 2 == 1:
            matching, rem = find_perfect_matching(N, cur_edges)
            for u, v, eid in matching:
                if eid < m:
                    ans[eid] = color_offset + d - 1
            color_graph(rem, d - 1, color_offset)
        else:
            g1, g2 = split_even(N, cur_edges)
            color_graph(g1, d // 2, color_offset)
            color_graph(g2, d // 2, color_offset + d // 2)

    color_graph(all_edges, D, 1)

    print("YES")
    print(*(ans[i] for i in range(m)))

if __name__ == '__main__':
    solve()