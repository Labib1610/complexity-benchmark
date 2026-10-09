import sys
import random
import time
import heapq
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    orders = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        orders.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))

    # Trivial sanity checks: single-commodity max-flow checks
    adj = [[] for _ in range(n + 1)]
    for i, (u, v, cap) in enumerate(edges):
        adj[u].append((v, cap, i))

    def max_flow(src, dst, max_needed):
        # Dinic's algorithm
        head = [[] for _ in range(n + 1)]
        edge_list = []
        def add_edge(u, v, c):
            head[u].append(len(edge_list))
            edge_list.append([v, c, 0])
            head[v].append(len(edge_list))
            edge_list.append([u, 0, 0])

        for u, v, c in edges:
            add_edge(u, v, c)

        flow = 0
        while flow < max_needed:
            level = [-1] * (n + 1)
            level[src] = 0
            q = deque([src])
            while q:
                u = q.popleft()
                for e_idx in head[u]:
                    v, cap, f = edge_list[e_idx]
                    if cap - f > 0 and level[v] == -1:
                        level[v] = level[u] + 1
                        q.append(v)
            if level[dst] == -1:
                break

            ptr = [0] * (n + 1)
            def dfs(u, push):
                if push == 0 or u == dst:
                    return push
                for cid in range(ptr[u], len(head[u])):
                    ptr[u] = cid
                    e_idx = head[u][cid]
                    v, cap, f = edge_list[e_idx]
                    tr = cap - f
                    if level[v] == level[u] + 1 and tr > 0:
                        pushed = dfs(v, min(push, tr))
                        if pushed > 0:
                            edge_list[e_idx][2] += pushed
                            edge_list[e_idx ^ 1][2] -= pushed
                            return pushed
                return 0

            while True:
                pushed = dfs(src, max_needed - flow)
                if pushed == 0:
                    break
                flow += pushed

        return flow

    for s, t, d in orders:
        if d > 0:
            if s == t:
                continue
            if max_flow(s, t, d) < d:
                print("NO")
                return

    # Check if total required flow on any cut is obviously violated
    # Let's use Negotiated Congestion Routing (Pathfinder algorithm)
    # Decompose demands into units or manageable chunks
    items = []
    for order_idx, (s, t, d) in enumerate(orders):
        if s == t or d == 0:
            continue
        # Split into unit paths or chunks
        rem = d
        while rem > 0:
            chunk = 1
            items.append((order_idx, s, t, chunk))
            rem -= chunk

    if not items:
        print("YES")
        for _ in range(k):
            print(*(0 for _ in range(m)))
        return

    # Negotiated Congestion Routing
    edge_usage = [0] * m
    history = [1.0] * m
    item_paths = [None] * len(items)

    adj_edges = [[] for _ in range(n + 1)]
    for i, (u, v, cap) in enumerate(edges):
        adj_edges[u].append((v, i))

    def find_path(src, dst, order_idx):
        dist = {src: 0.0}
        parent = {}
        pq = [(0.0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist.get(u, float('inf')):
                continue
            if u == dst:
                break
            for v, e_idx in adj_edges[u]:
                cap = edges[e_idx][2]
                occ = edge_usage[e_idx]
                pres_fac = 1.0 + max(0, occ + 1 - cap) * 2.0
                cost = history[e_idx] * pres_fac + random.uniform(0, 0.01)
                new_d = d + cost
                if new_d < dist.get(v, float('inf')):
                    dist[v] = new_d
                    parent[v] = (u, e_idx)

        if dst not in parent and src != dst:
            return None
        path = []
        curr = dst
        while curr != src:
            p, e_idx = parent[curr]
            path.append(e_idx)
            curr = p
        path.reverse()
        return path

    start_time = time.time()
    max_iter = 250
    success = False

    # Initial routing
    for idx, (order_idx, s, t, chunk) in enumerate(items):
        p = find_path(s, t, order_idx)
        if p is None:
            break
        item_paths[idx] = p
        for e_idx in p:
            edge_usage[e_idx] += chunk

    for iteration in range(max_iter):
        if time.time() - start_time > 4.2:
            break

        # Check overcapacity
        overcap = False
        for e_idx in range(m):
            if edge_usage[e_idx] > edges[e_idx][2]:
                overcap = True
                history[e_idx] += (edge_usage[e_idx] - edges[e_idx][2]) * 0.5

        if not overcap and all(p is not None for p in item_paths):
            success = True
            break

        # Rip up and reroute
        indices = list(range(len(items)))
        random.shuffle(indices)
        for idx in indices:
            order_idx, s, t, chunk = items[idx]
            old_p = item_paths[idx]
            if old_p is not None:
                for e_idx in old_p:
                    edge_usage[e_idx] -= chunk
            new_p = find_path(s, t, order_idx)
            if new_p is not None:
                item_paths[idx] = new_p
                for e_idx in new_p:
                    edge_usage[e_idx] += chunk
            else:
                if old_p is not None:
                    item_paths[idx] = old_p
                    for e_idx in old_p:
                        edge_usage[e_idx] += chunk

    if success:
        print("YES")
        res = [[0] * m for _ in range(k)]
        for idx, (order_idx, s, t, chunk) in enumerate(items):
            for e_idx in item_paths[idx]:
                res[order_idx][e_idx] += chunk
        for row in res:
            print(*(row))
    else:
        # Fallback ILP / Simplex check if small or output NO
        print("NO")

if __name__ == '__main__':
    solve()