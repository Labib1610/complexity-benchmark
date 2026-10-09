import sys
import collections
import heapq
import time
import random

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    orders = []
    for i in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        orders.append((s, t, d))
        
    edges = []
    adj = [[] for _ in range(n)]
    for j in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))
        adj[u].append((v, j, c))

    # Quick check: individual max-flow for each order
    def max_flow(src, dst, caps):
        # Dinic's algorithm
        head = [0] * n
        adj_flow = [[] for _ in range(n)]
        edge_list = []
        for j, (u, v, cap) in enumerate(edges):
            c_val = min(cap, caps[j])
            if c_val <= 0:
                continue
            e1 = [v, c_val, len(adj_flow[v])]
            e2 = [u, 0, len(adj_flow[u])]
            adj_flow[u].append(e1)
            adj_flow[v].append(e2)
            
        def bfs(s, t, level):
            for i in range(n):
                level[i] = -1
            level[s] = 0
            q = collections.deque([s])
            while q:
                curr = q.popleft()
                for v, cap, rev in adj_flow[curr]:
                    if cap > 0 and level[v] < 0:
                        level[v] = level[curr] + 1
                        q.append(v)
            return level[t] >= 0

        def dfs(curr, t, push, level, ptr):
            if curr == t or push == 0:
                return push
            for cid in range(ptr[curr], len(adj_flow[curr])):
                ptr[curr] = cid
                v, cap, rev = adj_flow[curr][cid]
                if level[v] == level[curr] + 1 and cap > 0:
                    tr = dfs(v, t, min(push, cap), level, ptr)
                    if tr > 0:
                        adj_flow[curr][cid][1] -= tr
                        adj_flow[v][rev][1] += tr
                        return tr
            return 0

        tot_flow = 0
        level = [-1] * n
        while bfs(src, dst, level):
            ptr = [0] * n
            while True:
                pushed = dfs(src, dst, float('inf'), level, ptr)
                if pushed == 0:
                    break
                tot_flow += pushed
        return tot_flow

    cap_list = [e[2] for e in edges]
    for i in range(k):
        s, t, d = orders[i]
        if d == 0:
            continue
        if max_flow(s, t, cap_list) < d:
            print("NO")
            return

    # If single order, max flow decomposition directly
    if k == 1:
        s, t, d = orders[0]
        # Find exact flow of size d
        # Using Dinic with capacity
        adj_flow = [[] for _ in range(n)]
        edge_indices = []
        for j, (u, v, cap) in enumerate(edges):
            e1 = [v, cap, len(adj_flow[v]), j]
            e2 = [u, 0, len(adj_flow[u]), -1]
            adj_flow[u].append(e1)
            adj_flow[v].append(e2)
            edge_indices.append((u, len(adj_flow[u]) - 1, e1))
            
        def bfs(s, dst, level):
            for i in range(n):
                level[i] = -1
            level[s] = 0
            q = collections.deque([s])
            while q:
                curr = q.popleft()
                for v, cap, rev, _ in adj_flow[curr]:
                    if cap > 0 and level[v] < 0:
                        level[v] = level[curr] + 1
                        q.append(v)
            return level[dst] >= 0

        def dfs(curr, dst, push, level, ptr):
            if curr == dst or push == 0:
                return push
            for cid in range(ptr[curr], len(adj_flow[curr])):
                ptr[curr] = cid
                v, cap, rev, idx = adj_flow[curr][cid]
                if level[v] == level[curr] + 1 and cap > 0:
                    tr = dfs(curr_dst:=v, dst, min(push, cap), level, ptr)
                    if tr > 0:
                        adj_flow[curr][cid][1] -= tr
                        adj_flow[v][rev][1] += tr
                        return tr
            return 0

        tot = 0
        level = [-1] * n
        while tot < d and bfs(s, t, level):
            ptr = [0] * n
            while tot < d:
                pushed = dfs(s, t, d - tot, level, ptr)
                if pushed == 0:
                    break
                tot += pushed
        if tot < d:
            print("NO")
            return
        ans = [0] * m
        for j, (u, v, cap) in enumerate(edges):
            # original cap - remaining cap
            for nxt, rem_cap, rev, e_idx in adj_flow[u]:
                if e_idx == j:
                    ans[j] = cap - rem_cap
                    break
        print("YES")
        print(*(ans))
        return

    # Multi-commodity flow: Local search / Multiplicative Weights Update
    # Decompose orders into unit paths (or chunks)
    unit_paths = [] # list of (order_id, path)
    for i, (s, t, d) in enumerate(orders):
        for _ in range(d):
            unit_paths.append((i, s, t, []))
            
    num_units = len(unit_paths)
    if num_units == 0:
        print("YES")
        for _ in range(k):
            print(*([0] * m))
        return

    # Edge usage count
    edge_usage = [0] * m

    def shortest_path(src, dst, weights):
        dist = [float('inf')] * n
        prev_edge = [-1] * n
        prev_node = [-1] * n
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d_u, u = heapq.heappop(pq)
            if d_u > dist[u]:
                continue
            if u == dst:
                break
            for v, j, _ in adj[u]:
                w = weights[j]
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev_edge[v] = j
                    prev_node[v] = u
                    heapq.heappush(pq, (dist[v], v))
        if dist[dst] == float('inf'):
            return None
        path = []
        curr = dst
        while curr != src:
            path.append(prev_edge[curr])
            curr = prev_node[curr]
        path.reverse()
        return path

    # Initial paths: shortest in hops
    base_weights = [1.0] * m
    paths = []
    for idx, (oid, s, t, _) in enumerate(unit_paths):
        p = shortest_path(s, t, base_weights)
        if p is None:
            print("NO")
            return
        paths.append(p)
        for e in p:
            edge_usage[e] += 1

    def compute_violation():
        viol = 0
        for j in range(m):
            if edge_usage[j] > cap_list[j]:
                viol += edge_usage[j] - cap_list[j]
        return viol

    start_time = time.time()
    best_viol = compute_violation()
    
    if best_viol == 0:
        pass
    else:
        # MWU / Simulated Annealing
        iterations = 0
        max_time = 4.5
        while best_viol > 0 and time.time() - start_time < max_time:
            iterations += 1
            
            # Find congested edges
            congested_edges = [j for j in range(m) if edge_usage[j] > cap_list[j]]
            if not congested_edges:
                best_viol = 0
                break
                
            # Pick a unit path that uses one of the most congested edges
            target_edge = random.choice(congested_edges)
            candidates = [u_idx for u_idx, p in enumerate(paths) if target_edge in p]
            if not candidates:
                u_idx = random.randint(0, num_units - 1)
            else:
                u_idx = random.choice(candidates)
                
            oid, s, t, _ = unit_paths[u_idx]
            old_path = paths[u_idx]
            for e in old_path:
                edge_usage[e] -= 1
                
            # Compute weights for Dijkstra
            # Base cost + exponential penalty for near/over capacity
            weights = [1.0] * m
            for j in range(m):
                c = cap_list[j]
                u = edge_usage[j]
                if c == 0:
                    weights[j] = 1e9
                elif u >= c:
                    weights[j] = 1.0 + 10.0 * (u - c + 1) ** 2 + random.random() * 0.1
                else:
                    weights[j] = 1.0 + (u / c) ** 2 + random.random() * 0.01

            new_path = shortest_path(s, t, weights)
            if new_path is None:
                new_path = old_path
                
            paths[u_idx] = new_path
            for e in new_path:
                edge_usage[e] += 1
                
            cur_viol = compute_violation()
            if cur_viol < best_viol:
                best_viol = cur_viol
                if best_viol == 0:
                    break

    if best_viol == 0:
        print("YES")
        order_edge_flow = [[0] * m for _ in range(k)]
        for u_idx, p in enumerate(paths):
            oid = unit_paths[u_idx][0]
            for e in p:
                order_edge_flow[oid][e] += 1
        for i in range(k):
            print(*(order_edge_flow[i]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()