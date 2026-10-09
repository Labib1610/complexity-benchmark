import sys
import heapq
import time
import random

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    
    compounds = []
    for _ in range(k):
        s = int(next(iterator)) - 1
        t = int(next(iterator)) - 1
        d = int(next(iterator))
        compounds.append((s, t, d))
        
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        cap = int(next(iterator))
        edges.append((u, v, cap))
        adj[u].append((v, i, cap))

    # Basic feasibility check using individual max flow
    def max_flow(src, dst, max_cap):
        # Dinic's algorithm
        head = [0] * n
        level = [-1] * n
        
        flow_edges = []
        g = [[] for _ in range(n)]
        
        for u, v, cap in edges:
            idx = len(flow_edges)
            flow_edges.append([v, cap, 0])
            flow_edges.append([u, 0, 0])
            g[u].append(idx)
            g[v].append(idx ^ 1)
            
        def bfs():
            for i in range(n):
                level[i] = -1
            level[src] = 0
            q = [src]
            qh = 0
            while qh < len(q):
                u = q[qh]
                qh += 1
                for edge_idx in g[u]:
                    v, cap, flow = flow_edges[edge_idx]
                    if cap - flow > 0 and level[v] == -1:
                        level[v] = level[u] + 1
                        q.append(v)
            return level[dst] != -1

        def dfs(u, pushed):
            if pushed == 0 or u == dst:
                return pushed
            for cid in range(head[u], len(g[u])):
                head[u] = cid
                edge_idx = g[u][cid]
                v, cap, flow = flow_edges[edge_idx]
                tr = cap - flow
                if level[u] + 1 != level[v] or tr == 0:
                    continue
                push = dfs(v, min(pushed, tr))
                if push == 0:
                    continue
                flow_edges[edge_idx][2] += push
                flow_edges[edge_idx ^ 1][2] -= push
                return push
            return 0

        tot = 0
        while bfs():
            head = [0] * n
            while True:
                p = dfs(src, 10**18)
                if p == 0:
                    break
                tot += p
        return tot

    for s, t, d in compounds:
        if s == t and d == 0:
            continue
        if max_flow(s, t, 0) < d:
            print("NO")
            return

    # Expand compounds into 1-unit units (or items)
    items = []
    for c_id, (s, t, d) in enumerate(compounds):
        for _ in range(d):
            items.append((c_id, s, t))
            
    T = len(items)
    if T == 0:
        print("YES")
        for _ in range(k):
            print(*(0 for _ in range(m)))
        return

    # Pathfinder / Negotiated Congestion routing
    # edge_usage[e]: total units currently on edge e
    edge_usage = [0] * m
    history_cost = [0.0] * m
    current_paths = [[] for _ in range(T)]

    start_time = time.time()
    
    # Initial routing
    for i, (c_id, s, t) in enumerate(items):
        dist = [float('inf')] * n
        parent = [None] * n
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            d_u, u = heapq.heappop(pq)
            if d_u > dist[u]:
                continue
            if u == t:
                break
            for v, e_idx, cap in adj[u]:
                cost = 1.0 + (edge_usage[e_idx] >= cap) * 10.0
                if dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    parent[v] = (u, e_idx)
        
        path = []
        curr = t
        while curr != s and parent[curr] is not None:
            p_u, e_idx = parent[curr]
            path.append(e_idx)
            curr = p_u
        path.reverse()
        current_paths[i] = path
        for e_idx in path:
            edge_usage[e_idx] += 1

    def is_feasible():
        for i in range(m):
            if edge_usage[i] > edges[i][2]:
                return False
        return True

    if is_feasible():
        ans = [[0] * m for _ in range(k)]
        for i, (c_id, s, t) in enumerate(items):
            for e_idx in current_paths[i]:
                ans[c_id][e_idx] += 1
        print("YES")
        for row in ans:
            print(*row)
        return

    # Iterative Rip-Up and Reroute
    max_iter = 400
    p_fac = 1.5
    
    for it in range(1, max_iter + 1):
        if time.time() - start_time > 4.5:
            break
            
        # Shuffle item processing order for randomness
        order = list(range(T))
        random.shuffle(order)
        
        for i in order:
            c_id, s, t = items[i]
            # Rip up
            for e_idx in current_paths[i]:
                edge_usage[e_idx] -= 1
                
            # Dijkstra to find best alternative path
            dist = [float('inf')] * n
            parent = [None] * n
            dist[s] = 0
            pq = [(0.0, s)]
            
            while pq:
                d_u, u = heapq.heappop(pq)
                if d_u > dist[u]:
                    continue
                if u == t:
                    break
                for v, e_idx, cap in adj[u]:
                    u_e = edge_usage[e_idx]
                    pres_cost = 0.0
                    if u_e + 1 > cap:
                        pres_cost = (u_e + 1 - cap) * p_fac * (1.0 + it * 0.2)
                    edge_c = 1.0 + history_cost[e_idx] + pres_cost
                    if dist[u] + edge_c < dist[v]:
                        dist[v] = dist[u] + edge_c
                        parent[v] = (u, e_idx)
                        
            path = []
            curr = t
            if dist[t] < float('inf'):
                while curr != s and parent[curr] is not None:
                    p_u, e_idx = parent[curr]
                    path.append(e_idx)
                    curr = p_u
                path.reverse()
            else:
                path = current_paths[i]
                
            current_paths[i] = path
            for e_idx in path:
                edge_usage[e_idx] += 1
                
        if is_feasible():
            ans = [[0] * m for _ in range(k)]
            for i, (c_id, s, t) in enumerate(items):
                for e_idx in current_paths[i]:
                    ans[c_id][e_idx] += 1
            print("YES")
            for row in ans:
                print(*row)
            return
            
        # Update history cost
        for e_idx in range(m):
            if edge_usage[e_idx] > edges[e_idx][2]:
                history_cost[e_idx] += (edge_usage[e_idx] - edges[e_idx][2]) * 0.5

    print("NO")

if __name__ == '__main__':
    solve()