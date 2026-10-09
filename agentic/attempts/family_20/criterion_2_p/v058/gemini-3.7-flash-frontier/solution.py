import sys
from collections import deque

# Increase recursion depth just in case
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n_L = int(input_data[0])
    n_R = int(input_data[1])
    m = int(input_data[2])
    
    orig_u = [0] * m
    orig_v = [0] * m
    deg_L = [0] * (n_L + 1)
    deg_R = [0] * (n_R + 1)
    
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        orig_u[i] = u
        orig_v[i] = v
        deg_L[u] += 1
        deg_R[v] += 1
        
    peak_load = 0
    for u in range(1, n_L + 1):
        if deg_L[u] > peak_load:
            peak_load = deg_L[u]
    for v in range(1, n_R + 1):
        if deg_R[v] > peak_load:
            peak_load = deg_R[v]
            
    ans = [0] * m
    if m == 0:
        print("YES")
        print()
        return

    def run_dinic(num_nodes, s, t, edge_list_dinic):
        adj = [[] for _ in range(num_nodes)]
        edges = []
        
        for u, v, cap, e_idx in edge_list_dinic:
            fwd_idx = len(edges)
            rev_idx = fwd_idx + 1
            edges.append([v, cap, rev_idx, e_idx, cap]) # [to, cap, rev, orig_edge_idx, orig_cap]
            edges.append([u, 0, fwd_idx, -1, 0])
            adj[u].append(fwd_idx)
            adj[v].append(rev_idx)
            
        level = [-1] * num_nodes
        head = [0] * num_nodes
        
        def bfs():
            for i in range(num_nodes):
                level[i] = -1
            level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for edge_idx in adj[u]:
                    v, cap, _, _, _ = edges[edge_idx]
                    if cap > 0 and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            return level[t] != -1

        def dfs(u):
            if u == t:
                return True
            while head[u] < len(adj[u]):
                edge_idx = adj[u][head[u]]
                v, cap, rev, _, _ = edges[edge_idx]
                if cap > 0 and level[v] == level[u] + 1:
                    if dfs(v):
                        edges[edge_idx][1] -= 1
                        edges[rev][1] += 1
                        return True
                head[u] += 1
            return False

        while bfs():
            for i in range(num_nodes):
                head[i] = 0
            while dfs(s):
                pass
                
        return edges

    def extract_matching(edge_indices, delta):
        cur_deg_L = {}
        cur_deg_R = {}
        for e in edge_indices:
            u = orig_u[e]
            v = orig_v[e]
            cur_deg_L[u] = cur_deg_L.get(u, 0) + 1
            cur_deg_R[v] = cur_deg_R.get(v, 0) + 1
            
        S_L = [u for u, d in cur_deg_L.items() if d == delta]
        S_R = [v for v, d in cur_deg_R.items() if d == delta]
        
        s = 0
        t = n_L + n_R + 1
        num_nodes = t + 1
        
        # Step 1: Match S_L
        dinic_edges = []
        for u in S_L:
            dinic_edges.append((s, u, 1, -1))
        for e in edge_indices:
            u = orig_u[e]
            v = orig_v[e]
            dinic_edges.append((u, n_L + v, 1, e))
        for v in cur_deg_R:
            dinic_edges.append((n_L + v, t, 1, -1))
            
        res_edges = run_dinic(num_nodes, s, t, dinic_edges)
        
        matched_edges = set()
        matched_R = {}
        matched_L = {}
        
        for v_to, cap, rev_idx, e_idx, orig_cap in res_edges:
            if e_idx >= 0 and orig_cap == 1 and cap == 0:
                matched_edges.add(e_idx)
                u = orig_u[e_idx]
                v = orig_v[e_idx]
                matched_L[u] = e_idx
                matched_R[v] = e_idx

        # Step 2: Match remaining S_R
        U_R = [v for v in S_R if v not in matched_R]
        if U_R:
            dinic_edges2 = []
            for v in U_R:
                dinic_edges2.append((s, n_L + v, 1, -1))
            for e in edge_indices:
                u = orig_u[e]
                v = orig_v[e]
                if e in matched_edges:
                    dinic_edges2.append((u, n_L + v, 1, e)) # L to R for matched
                else:
                    dinic_edges2.append((n_L + v, u, 1, e)) # R to L for non-matched
            for u in cur_deg_L:
                if u not in matched_L:
                    dinic_edges2.append((u, t, 1, -1))
                    
            res_edges2 = run_dinic(num_nodes, s, t, dinic_edges2)
            for v_to, cap, rev_idx, e_idx, orig_cap in res_edges2:
                if e_idx >= 0 and orig_cap == 1 and cap == 0:
                    if e_idx in matched_edges:
                        matched_edges.remove(e_idx)
                    else:
                        matched_edges.add(e_idx)
                        
        return matched_edges

    def euler_split(edge_indices):
        cur_deg_L = {}
        cur_deg_R = {}
        for e in edge_indices:
            u = orig_u[e]
            v = orig_v[e]
            cur_deg_L[u] = cur_deg_L.get(u, 0) + 1
            cur_deg_R[v] = cur_deg_R.get(v, 0) + 1
            
        O_L = [u for u, d in cur_deg_L.items() if d % 2 == 1]
        O_R = [v for v, d in cur_deg_R.items() if d % 2 == 1]
        
        k = min(len(O_L), len(O_R))
        dummy_edges = []
        for i in range(k):
            dummy_edges.append((O_L[i], n_L + O_R[i]))
            
        rem_L = O_L[k:]
        rem_R = O_R[k:]
        
        next_dummy_R = n_L + n_R + 1
        for i in range(0, len(rem_L), 2):
            d_node = next_dummy_R
            next_dummy_R += 1
            dummy_edges.append((rem_L[i], d_node))
            dummy_edges.append((rem_L[i+1], d_node))
            
        next_dummy_L = next_dummy_R
        for i in range(0, len(rem_R), 2):
            d_node = next_dummy_L
            next_dummy_L += 1
            dummy_edges.append((d_node, n_L + rem_R[i]))
            dummy_edges.append((d_node, n_L + rem_R[i+1]))
            
        total_nodes = next_dummy_L + 1
        adj = [[] for _ in range(total_nodes)]
        
        total_edges_count = len(edge_indices) + len(dummy_edges)
        used = [False] * total_edges_count
        
        for internal_id, e in enumerate(edge_indices):
            u = orig_u[e]
            v = n_L + orig_v[e]
            adj[u].append((v, internal_id, e))
            adj[v].append((u, internal_id, e))
            
        for d_id, (u, v) in enumerate(dummy_edges):
            internal_id = len(edge_indices) + d_id
            adj[u].append((v, internal_id, -1))
            adj[v].append((u, internal_id, -1))
            
        head = [0] * total_nodes
        E1 = []
        E2 = []
        
        # All L-side nodes have index <= n_L or are dummy L nodes
        # Nodes in R-side have index > n_L and < next_dummy_L (except dummy L nodes)
        # To be precise: u is L-side if u <= n_L or (u >= next_dummy_R and u < next_dummy_L ... wait, next_dummy_L is L-nodes)
        # Let's cleanly check if a node is in L:
        def is_left(node):
            if 1 <= node <= n_L:
                return True
            if next_dummy_R <= node < next_dummy_L:
                return False # dummy R
            if node >= next_dummy_L:
                return True  # dummy L
            return False     # original R (n_L + 1 .. n_L + n_R)

        for start_node in range(total_nodes):
            if head[start_node] < len(adj[start_node]):
                stack = [start_node]
                while stack:
                    u = stack[-1]
                    while head[u] < len(adj[u]) and used[adj[u][head[u]][1]]:
                        head[u] += 1
                    if head[u] < len(adj[u]):
                        v, internal_id, orig_id = adj[u][head[u]]
                        used[internal_id] = True
                        head[u] += 1
                        if orig_id != -1:
                            if is_left(u):
                                E1.append(orig_id)
                            else:
                                E2.append(orig_id)
                        stack.append(v)
                    else:
                        stack.pop()
                        
        return E1, E2

    # Recursive solver
    tasks = [(list(range(m)), 0, peak_load)]
    while tasks:
        edge_list, color_offset, delta = tasks.pop()
        if not edge_list or delta == 0:
            continue
        if delta == 1:
            for e in edge_list:
                ans[e] = color_offset + 1
            continue
        if delta % 2 == 1:
            matching = extract_matching(edge_list, delta)
            for e in matching:
                ans[e] = color_offset + delta
            edge_list = [e for e in edge_list if e not in matching]
            delta -= 1
            if delta == 0:
                continue
                
        E1, E2 = euler_split(edge_list)
        half_delta = delta // 2
        tasks.append((E2, color_offset + half_delta, half_delta))
        tasks.append((E1, color_offset, half_delta))

    print("YES")
    print(*(ans[i] for i in range(m)))

if __name__ == '__main__':
    solve()