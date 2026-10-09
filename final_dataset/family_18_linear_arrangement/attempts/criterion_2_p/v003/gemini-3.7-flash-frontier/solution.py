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

    start_time = time.time()
    time_limit = 4.3

    def eval_cost(pos):
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
        return cost

    def make_pos(order):
        pos = [0] * (n + 1)
        for p, u in enumerate(order, 1):
            pos[u] = p
        return pos

    best_cost = float('inf')
    best_pos = None

    def update_best(pos):
        nonlocal best_cost, best_pos
        c = eval_cost(pos)
        if c < best_cost:
            best_cost = c
            best_pos = list(pos)
        return c <= B

    # Heuristic 1: Centroid Recursive Bisection
    def get_centroid_order():
        visited = [False] * (n + 1)
        sz = [0] * (n + 1)

        def get_sizes(u, p):
            sz[u] = 1
            for v in adj[u]:
                if v != p and not visited[v]:
                    get_sizes(v, u)
                    sz[u] += sz[v]

        def get_centroid(u, p, total):
            for v in adj[u]:
                if v != p and not visited[v]:
                    if sz[v] > total // 2:
                        return get_centroid(v, u, total)
            return u

        def decompose(u):
            get_sizes(u, 0)
            total = sz[u]
            c = get_centroid(u, 0, total)
            visited[c] = True

            comp_orders = []
            for v in adj[c]:
                if not visited[v]:
                    comp_orders.append(decompose(v))

            left = []
            right = []
            l_sz, r_sz = 0, 0
            # Sort components by size descending for balanced partition
            comp_orders.sort(key=len, reverse=True)
            for comp in comp_orders:
                if l_sz <= r_sz:
                    left.extend(comp)
                    l_sz += len(comp)
                else:
                    right.extend(comp)
                    r_sz += len(comp)

            visited[c] = False
            return left + [c] + right

        return decompose(1)

    order1 = get_centroid_order()
    pos1 = make_pos(order1)
    if update_best(pos1):
        print("YES")
        print(*(best_pos[1:]))
        return

    # Heuristic 2: DFS in-order layouts from multiple roots
    roots_to_try = [1]
    # Add high degree nodes
    degrees = sorted(range(1, n + 1), key=lambda x: len(adj[x]), reverse=True)
    roots_to_try.extend(degrees[:min(5, n)])

    for root in set(roots_to_try):
        if time.time() - start_time > time_limit:
            break
        order = []
        vis = [False] * (n + 1)
        
        def dfs(u):
            vis[u] = True
            children = [v for v in adj[u] if not vis[v]]
            half = len(children) // 2
            for v in children[:half]:
                dfs(v)
            order.append(u)
            for v in children[half:]:
                dfs(v)

        dfs(root)
        pos = make_pos(order)
        if update_best(pos):
            print("YES")
            print(*(best_pos[1:]))
            return

    # Local Search / Simulated Annealing
    pos = list(best_pos)
    cur_order = [0] * n
    for i in range(1, n + 1):
        cur_order[pos[i] - 1] = i

    cur_cost = best_cost
    T = max(1.0, float(cur_cost) * 0.1)
    T_min = 0.01
    alpha = 0.99995

    # Pre-build edge list for fast delta evaluation
    adj_no_v = adj

    steps = 0
    while time.time() - start_time < time_limit:
        steps += 1
        # Pick two positions to swap or pick a vertex and shift
        i = random.randint(1, n)
        j = random.randint(1, n)
        if i == j:
            continue

        p_i = pos[i]
        p_j = pos[j]

        # Calculate delta
        delta = 0
        for w in adj[i]:
            if w != j:
                delta += abs(p_j - pos[w]) - abs(p_i - pos[w])
        for w in adj[j]:
            if w != i:
                delta += abs(p_i - pos[w]) - abs(p_j - pos[w])

        if delta < 0 or (T > 0 and random.random() < 2.718281828459045 ** (-delta / T)):
            pos[i], pos[j] = p_j, p_i
            cur_cost += delta
            if cur_cost < best_cost:
                best_cost = cur_cost
                best_pos = list(pos)
                if best_cost <= B:
                    print("YES")
                    print(*(best_pos[1:]))
                    return

        T = max(T_min, T * 0.99998)

    if best_cost <= B:
        print("YES")
        print(*(best_pos[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()