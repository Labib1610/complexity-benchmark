import sys
import time
import random

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    if n == 1:
        if B >= 0:
            print("YES")
            print("1")
        else:
            print("NO")
        return

    adj = [[] for _ in range(n + 1)]
    edges = []
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        idx += 2

    # Helper to compute cost of a layout
    # pos[u] is the 1-based slot of qubit u
    def compute_cost(pos):
        c = 0
        for u, v in edges:
            c += abs(pos[u] - pos[v])
        return c

    best_cost = float('inf')
    best_layout = None

    def update_best(order):
        nonlocal best_cost, best_layout
        pos = [0] * (n + 1)
        for i, u in enumerate(order):
            pos[u] = i + 1
        c = compute_cost(pos)
        if c < best_cost:
            best_cost = c
            best_layout = pos
        return c

    # Heuristic 1: Centroid-based tree layout
    sz = [0] * (n + 1)
    def get_sizes(u, p):
        sz[u] = 1
        for v in adj[u]:
            if v != p:
                get_sizes(v, u)
                sz[u] += sz[v]

    def get_centroid(u, p, total):
        for v in adj[u]:
            if v != p and sz[v] > total // 2:
                return get_centroid(v, u, total)
        return u

    get_sizes(1, 0)
    centroid = get_centroid(1, 0, n)

    # Generate tree orders rooted at various roots
    candidates = [centroid, 1]
    # Add nodes with high degrees
    degs = sorted(range(1, n + 1), key=lambda x: len(adj[x]), reverse=True)
    candidates.extend(degs[:min(10, n)])
    candidates = list(dict.fromkeys(candidates))

    def build_tree_order(root):
        get_sizes(root, 0)
        order = []
        
        def place(u, p, side):
            children = [v for v in adj[u] if v != p]
            children.sort(key=lambda x: sz[x])
            
            left_c = []
            right_c = []
            for i, c in enumerate(children):
                if i % 2 == 0:
                    left_c.append(c)
                else:
                    right_c.append(c)
            
            # If side == 0 (root), place left, then u, then right
            # If side == -1 (u must be near right edge of its block), place children to left
            # If side == 1 (u must be near left edge of its block), place children to right
            res = []
            if side == 0:
                for c in left_c:
                    res.extend(place(c, u, -1))
                res.append(u)
                for c in right_c:
                    res.extend(place(c, u, 1))
            elif side == -1:
                for c in children:
                    res.extend(place(c, u, -1))
                res.append(u)
            else:
                res.append(u)
                for c in children:
                    res.extend(place(c, u, 1))
            return res

        return place(root, 0, 0)

    for r in candidates:
        ord_r = build_tree_order(r)
        if len(ord_r) == n:
            update_best(ord_r)
            if best_cost <= B:
                break

    # Heuristic 2: BFS and DFS orders
    if best_cost > B:
        for r in candidates:
            # DFS
            visited = [False] * (n + 1)
            dfs_order = []
            stack = [r]
            while stack:
                curr = stack.pop()
                if not visited[curr]:
                    visited[curr] = True
                    dfs_order.append(curr)
                    for nxt in adj[curr]:
                        if not visited[nxt]:
                            stack.append(nxt)
            update_best(dfs_order)
            if best_cost <= B:
                break

            # BFS
            visited = [False] * (n + 1)
            bfs_order = []
            queue = [r]
            visited[r] = True
            q_idx = 0
            while q_idx < len(queue):
                curr = queue[q_idx]
                q_idx += 1
                bfs_order.append(curr)
                for nxt in adj[curr]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        queue.append(nxt)
            update_best(bfs_order)
            if best_cost <= B:
                break

    # Simulated Annealing / Local Search to improve if not yet <= B
    start_time = time.time()
    time_limit = 4.0

    if best_cost > B and best_layout is not None:
        # Convert best_layout to order array (0-indexed)
        # order[slot-1] = qubit
        order = [0] * n
        for u in range(1, n + 1):
            order[best_layout[u] - 1] = u
        
        # Position lookup
        pos = list(best_layout)

        cur_cost = best_cost
        T = 5.0
        T_min = 0.01
        alpha = 0.9995

        iter_count = 0
        while time.time() - start_time < time_limit and cur_cost > B:
            iter_count += 1
            if iter_count % 1000 == 0:
                T = max(T_min, T * alpha)

            # Pick two vertices to swap
            # Either adjacent in order, or random pair, or connected pair
            r_type = random.random()
            if r_type < 0.4:
                # Adjacent in slot
                i = random.randint(0, n - 2)
                j = i + 1
            elif r_type < 0.7:
                # Connected vertices: swap one with something between them
                u, v = random.choice(edges)
                p1, p2 = pos[u] - 1, pos[v] - 1
                if abs(p1 - p2) > 1:
                    i = min(p1, p2)
                    j = random.randint(i + 1, max(p1, p2))
                else:
                    i = random.randint(0, n - 1)
                    j = random.randint(0, n - 1)
            else:
                i = random.randint(0, n - 1)
                j = random.randint(0, n - 1)

            if i == j:
                continue

            u, v = order[i], order[j]
            # Calculate change in cost
            # Cost change only depends on edges incident to u and v
            old_c = 0
            for w in adj[u]:
                old_c += abs(pos[u] - pos[w])
            for w in adj[v]:
                if w != u:
                    old_c += abs(pos[v] - pos[w])

            # New positions
            pos[u], pos[v] = pos[v], pos[u]
            new_c = 0
            for w in adj[u]:
                new_c += abs(pos[u] - pos[w])
            for w in adj[v]:
                if w != u:
                    new_c += abs(pos[v] - pos[w])

            delta = new_c - old_c
            if delta <= 0 or (T > 0 and random.random() < 2.718281828459045 ** (-delta / T)):
                cur_cost += delta
                order[i], order[j] = v, u
                if cur_cost < best_cost:
                    best_cost = cur_cost
                    best_layout = list(pos)
                    if best_cost <= B:
                        break
            else:
                # Revert
                pos[u], pos[v] = pos[v], pos[u]

    if best_cost <= B:
        print("YES")
        print(*(best_layout[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()