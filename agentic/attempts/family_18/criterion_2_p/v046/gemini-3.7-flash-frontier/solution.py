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

    if n <= 1:
        print("YES")
        print("1")
        return

    def compute_cost(pos):
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
        return cost

    def make_pos(order):
        pos = [0] * (n + 1)
        for i, u in enumerate(order):
            pos[u] = i + 1
        return pos

    # Tree-based heuristic: rooted tree layout
    def tree_layout(root):
        # Layout rooted tree
        # For each node, partition children into left and right to balance sizes
        sz = [0] * (n + 1)
        parent = [0] * (n + 1)
        order_bfs = []
        stack = [root]
        visited = [False] * (n + 1)
        visited[root] = True
        
        # Post-order for size
        q = [root]
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        
        for u in reversed(q):
            sz[u] = 1
            for v in adj[u]:
                if v != parent[u]:
                    sz[u] += sz[v]
                    
        def layout_node(u):
            children = [v for v in adj[u] if v != parent[u]]
            if not children:
                return [u]
            children.sort(key=lambda c: sz[c], reverse=True)
            left_children = []
            right_children = []
            left_sum = 0
            right_sum = 0
            for c in children:
                if left_sum <= right_sum:
                    left_children.append(c)
                    left_sum += sz[c]
                else:
                    right_children.append(c)
                    right_sum += sz[c]
            
            res_left = []
            for c in reversed(left_children):
                res_left.extend(layout_node(c))
            res_right = []
            for c in right_children:
                res_right.extend(layout_node(c))
            return res_left + [u] + res_right

        return layout_node(root)

    best_order = None
    best_cost = float('inf')

    # Try various roots
    roots_to_try = list(range(1, n + 1))
    if len(roots_to_try) > 60:
        # Sample roots: degrees, random
        deg_sorted = sorted(range(1, n + 1), key=lambda x: len(adj[x]), reverse=True)
        roots_to_try = deg_sorted[:30] + random.sample(range(1, n + 1), 30)

    for r in roots_to_try:
        order = tree_layout(r)
        pos = make_pos(order)
        cost = compute_cost(pos)
        if cost < best_cost:
            best_cost = cost
            best_order = order
            if best_cost <= B:
                break

    if best_cost <= B:
        print("YES")
        pos = make_pos(best_order)
        print(*(pos[i] for i in range(1, n + 1)))
        return

    # Simulated Annealing / Local Search with adjacent swaps
    start_time = time.time()
    order = list(best_order)
    pos = make_pos(order)
    current_cost = best_cost

    # Pre-structure for fast delta
    # order is 0-indexed: order[0] to order[n-1]
    # pos is 0-indexed internally for speed: pos[u] in 0..n-1
    pos_arr = [pos[i] - 1 for i in range(n + 1)]

    # SA parameters
    T = 5.0
    T_min = 1e-4
    alpha = 0.99995

    iter_count = 0
    while time.time() - start_time < 4.2:
        iter_count += 1
        i = random.randint(0, n - 2)
        u = order[i]
        v = order[i + 1]

        # Delta calculation for swapping order[i] (u) and order[i+1] (v)
        # u moves from i to i+1:
        # for w in adj[u], w != v: if pos[w] < i -> +1, if pos[w] > i+1 -> -1
        # v moves from i+1 to i:
        # for w in adj[v], w != u: if pos[w] < i -> -1, if pos[w] > i+1 -> +1
        delta = 0
        for w in adj[u]:
            if w != v:
                pw = pos_arr[w]
                if pw < i:
                    delta += 1
                elif pw > i + 1:
                    delta -= 1
        for w in adj[v]:
            if w != u:
                pw = pos_arr[w]
                if pw < i:
                    delta -= 1
                elif pw > i + 1:
                    delta += 1

        accept = False
        if delta <= 0:
            accept = True
        else:
            if T > 1e-6 and random.random() < 2.718281828459045 ** (-delta / T):
                accept = True

        if accept:
            order[i], order[i + 1] = v, u
            pos_arr[u] = i + 1
            pos_arr[v] = i
            current_cost += delta

            if current_cost < best_cost:
                best_cost = current_cost
                best_order = list(order)
                if best_cost <= B:
                    break

        T = max(T_min, T * alpha)
        if iter_count % 50000 == 0:
            T = max(T, 1.0)  # reheat slightly

    if best_cost <= B:
        print("YES")
        pos = make_pos(best_order)
        print(*(pos[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()