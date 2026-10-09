import sys
import time

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
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        idx += 2

    if n == 1:
        print("YES")
        print("1")
        return

    start_time = time.time()

    # Find centroids or candidate roots
    def get_subtree_sizes(root):
        sz = [0] * (n + 1)
        parent = [0] * (n + 1)
        order = []
        stack = [root]
        visited = [False] * (n + 1)
        visited[root] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)
        for u in reversed(order):
            sz[u] = 1
            for v in adj[u]:
                if v != parent[u]:
                    sz[u] += sz[v]
        return sz, parent, order

    # Compute optimal layout given a root
    def compute_layout(root):
        sz, parent, order = get_subtree_sizes(root)
        
        # We will determine the Left/Right children partition for each node
        # For each node u, we want to partition children into L and R.
        # L children sorted by sz descending, R children sorted by sz ascending.
        # DP state: child assignment
        children_split = {} # u -> (L_children, R_children)
        
        for u in reversed(order):
            ch = [v for v in adj[u] if v != parent[u]]
            if not ch:
                children_split[u] = ([], [])
                continue
            
            # Sort children by size descending
            ch.sort(key=lambda v: sz[v], reverse=True)
            
            # Partition children into two sets to balance sizes
            L = []
            R = []
            sum_L = 0
            sum_R = 0
            for v in ch:
                if sum_L <= sum_R:
                    L.append(v)
                    sum_L += sz[v]
                else:
                    R.append(v)
                    sum_R += sz[v]
            
            # Sort L descending by size, R ascending by size
            L.sort(key=lambda v: sz[v], reverse=True)
            R.sort(key=lambda v: sz[v])
            children_split[u] = (L, R)

        # Reconstruct vertex order
        res_order = []
        def build(u, side):
            L, R = children_split[u]
            if side == 'L':
                for v in L:
                    build(v, 'L')
                res_order.append(u)
                for v in R:
                    build(v, 'R')
            else:
                for v in L:
                    build(v, 'L')
                res_order.append(u)
                for v in R:
                    build(v, 'R')

        build(root, 'C')
        return res_order

    def eval_cost(order_list):
        pos = [0] * (n + 1)
        for i, u in enumerate(order_list):
            pos[u] = i + 1
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
        return cost, pos

    # Select candidate roots (centroids, high-degree nodes, random)
    sz1, _, _ = get_subtree_sizes(1)
    # Find centroid
    curr = 1
    p = 0
    while True:
        moved = False
        for v in adj[curr]:
            if v != p and sz1[v] > n // 2:
                p = curr
                curr = v
                moved = True
                break
        if not moved:
            break
    centroid = curr

    candidates = [centroid]
    # Add other high degree nodes and neighbors of centroid
    deg_nodes = sorted(range(1, n + 1), key=lambda x: len(adj[x]), reverse=True)
    candidates.extend(deg_nodes[:min(n, 10)])
    candidates.extend(adj[centroid])
    candidates = list(dict.fromkeys(candidates))

    best_cost = float('inf')
    best_pos = None

    for r in candidates:
        order_list = compute_layout(r)
        cost, pos = eval_cost(order_list)
        if cost < best_cost:
            best_cost = cost
            best_pos = pos
            if best_cost <= B:
                break
        if time.time() - start_time > 1.5:
            break

    # If already <= B, we are done
    if best_cost <= B:
        print("YES")
        print(*(best_pos[1:]))
        return

    # Local search to improve the arrangement
    # Node at position p: inv[p]
    inv = [0] * (n + 1)
    for u in range(1, n + 1):
        inv[best_pos[u]] = u

    import random
    cur_cost = best_cost
    pos = list(best_pos)

    # Hill climbing / simulated annealing
    step = 0
    while time.time() - start_time < 4.5:
        step += 1
        # Pick two positions to swap
        i = random.randint(1, n)
        # Prefer swapping nearby positions or connected nodes
        if random.random() < 0.5 and len(edges) > 0:
            e = random.choice(edges)
            u, v = e
            i, j = pos[u], pos[v]
            if i > j:
                i, j = j, i
            if j - i > 1:
                j = i + 1
        else:
            j = random.randint(max(1, i - 10), min(n, i + 10))
        
        if i == j:
            continue

        u = inv[i]
        v = inv[j]

        # Calculate cost change
        delta = 0
        for neighbor in adj[u]:
            if neighbor != v:
                delta -= abs(pos[u] - pos[neighbor])
                delta += abs(pos[v] - pos[neighbor])
        for neighbor in adj[v]:
            if neighbor != u:
                delta -= abs(pos[v] - neighbor_pos := pos[neighbor])
                delta += abs(pos[u] - neighbor_pos)

        if delta <= 0:
            cur_cost += delta
            pos[u], pos[v] = pos[v], pos[u]
            inv[i], inv[j] = v, u
            if cur_cost < best_cost:
                best_cost = cur_cost
                best_pos = list(pos)
                if best_cost <= B:
                    print("YES")
                    print(*(best_pos[1:]))
                    return

    if best_cost <= B:
        print("YES")
        print(*(best_pos[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()