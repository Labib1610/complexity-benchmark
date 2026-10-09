import sys
import time
import random
import math

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
            print(1)
        else:
            print("NO")
        return

    adj = [[] for _ in range(n)]
    edges = []
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    deg = [len(adj[i]) for i in range(n)]

    def compute_cost(pos):
        return sum(abs(pos[u] - pos[v]) for u, v in edges)

    best_cost = float('inf')
    best_pos = None

    def check_and_save(pos):
        nonlocal best_cost, best_pos
        c = compute_cost(pos)
        if c < best_cost:
            best_cost = c
            best_pos = list(pos)
        return c <= B

    # 1. Centroid-based recursive layout
    def get_centroid_layout():
        sz = [0] * n
        removed = [False] * n

        def get_sizes(u, p):
            sz[u] = 1
            for v in adj[u]:
                if v != p and not removed[v]:
                    get_sizes(v, u)
                    sz[u] += sz[v]

        def get_centroid(u, p, total):
            for v in adj[u]:
                if v != p and not removed[v] and sz[v] > total // 2:
                    return get_centroid(v, u, total)
            return u

        def decompose(root):
            get_sizes(root, -1)
            c = get_centroid(root, -1, sz[root])
            removed[c] = True
            
            sub_layouts = []
            for v in adj[c]:
                if not removed[v]:
                    sub_layouts.append(decompose(v))
            
            # Split sub_layouts into left and right to balance sizes
            sub_layouts.sort(key=len, reverse=True)
            left, right = [], []
            len_l, len_r = 0, 0
            for sl in sub_layouts:
                if len_l <= len_r:
                    left.extend(sl)
                    len_l += len(sl)
                else:
                    right.extend(sl)
                    len_r += len(sl)
            
            return left + [c] + right

        order = decompose(0)
        pos = [0] * n
        for p, u in enumerate(order, 1):
            pos[u] = p
        return pos

    # 2. Spectral (Fiedler vector) layout
    def get_spectral_layout():
        alpha = max(deg) + 2.0
        x = [random.uniform(-1.0, 1.0) for _ in range(n)]
        mean_x = sum(x) / n
        x = [v - mean_x for v in x]

        for _ in range(150):
            y = [0.0] * n
            for u in range(n):
                s = sum(x[v] for v in adj[u])
                y[u] = (alpha - deg[u]) * x[u] + s
            mean_y = sum(y) / n
            norm_sq = 0.0
            for u in range(n):
                y[u] -= mean_y
                norm_sq += y[u] * y[u]
            if norm_sq < 1e-12:
                break
            inv_norm = 1.0 / math.sqrt(norm_sq)
            x = [val * inv_norm for val in y]

        order = sorted(range(n), key=lambda u: x[u])
        pos = [0] * n
        for p, u in enumerate(order, 1):
            pos[u] = p
        return pos

    # 3. BFS / DFS layout from diameter ends
    def get_tree_layout(root, method='dfs'):
        order = []
        visited = [False] * n
        if method == 'dfs':
            stack = [root]
            while stack:
                u = stack.pop()
                if not visited[u]:
                    visited[u] = True
                    order.append(u)
                    for v in adj[u]:
                        if not visited[v]:
                            stack.append(v)
        else:
            from collections import deque
            q = deque([root])
            visited[root] = True
            while q:
                u = q.popleft()
                order.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
        pos = [0] * n
        for p, u in enumerate(order, 1):
            pos[u] = p
        return pos

    # Find tree diameter endpoints
    def find_farthest(start):
        dist = [-1] * n
        dist[start] = 0
        q = [start]
        for u in q:
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        farthest = max(range(n), key=lambda u: dist[u])
        return farthest, dist[farthest]

    u_end, _ = find_farthest(0)
    v_end, _ = find_farthest(u_end)

    initial_layouts = [
        get_centroid_layout(),
        get_spectral_layout(),
        get_tree_layout(u_end, 'dfs'),
        get_tree_layout(v_end, 'dfs'),
        get_tree_layout(u_end, 'bfs'),
    ]

    for pos in initial_layouts:
        if check_and_save(pos):
            print("YES")
            print(*(best_pos[i] for i in range(n)))
            return

    # Local search with Simulated Annealing
    start_time = time.time()
    time_limit = 4.3

    current_pos = list(best_pos)
    inv = [0] * (n + 1)
    for u in range(n):
        inv[current_pos[u]] = u

    current_cost = best_cost
    T = max(1.0, current_cost * 0.05)
    T_min = 1e-3
    decay = 0.99995

    iterations = 0
    while time.time() - start_time < time_limit:
        iterations += 1
        if iterations % 1000 == 0:
            if current_cost <= B:
                break

        # Randomly choose swap or relocate
        move_type = random.random()
        if move_type < 0.6:
            # Swap two positions
            if random.random() < 0.5:
                # Swap adjacent in arrangement
                p1 = random.randint(1, n - 1)
                p2 = p1 + 1
            else:
                p1 = random.randint(1, n)
                p2 = random.randint(1, n)
                if p1 == p2:
                    continue

            u = inv[p1]
            v = inv[p2]

            # Delta cost of swapping pos of u and v
            delta = 0
            for w in adj[u]:
                if w != v:
                    delta += abs(p2 - current_pos[w]) - abs(p1 - current_pos[w])
            for w in adj[v]:
                if w != u:
                    delta += abs(p1 - current_pos[w]) - abs(p2 - current_pos[w])

            if delta < 0 or math.exp(-delta / max(T, 1e-6)) > random.random():
                current_cost += delta
                current_pos[u] = p2
                current_pos[v] = p1
                inv[p1] = v
                inv[p2] = u
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_pos = list(current_pos)
                    if best_cost <= B:
                        break
        else:
            # Relocate a vertex u to a new position target_p
            u = random.randint(0, n - 1)
            src_p = current_pos[u]
            target_p = random.randint(1, n)
            if src_p == target_p:
                continue

            # Calculate delta for shifting u to target_p
            if src_p < target_p:
                # Vertices at src_p+1..target_p shift left by 1
                delta = 0
                for w in adj[u]:
                    pw = current_pos[w]
                    delta += abs(target_p - (pw - 1 if src_p < pw <= target_p else pw)) - abs(src_p - pw)
                for p in range(src_p + 1, target_p + 1):
                    w = inv[p]
                    if w == u:
                        continue
                    pw_old = p
                    pw_new = p - 1
                    for nb in adj[w]:
                        if nb == u:
                            continue
                        p_nb = current_pos[nb]
                        delta += abs(pw_new - p_nb) - abs(pw_old - p_nb)
            else:
                # Vertices at target_p..src_p-1 shift right by 1
                delta = 0
                for w in adj[u]:
                    pw = current_pos[w]
                    delta += abs(target_p - (pw + 1 if target_p <= pw < src_p else pw)) - abs(src_p - pw)
                for p in range(target_p, src_p):
                    w = inv[p]
                    if w == u:
                        continue
                    pw_old = p
                    pw_new = p + 1
                    for nb in adj[w]:
                        if nb == u:
                            continue
                        p_nb = current_pos[nb]
                        delta += abs(pw_new - p_nb) - abs(pw_old - p_nb)

            if delta < 0 or math.exp(-delta / max(T, 1e-6)) > random.random():
                current_cost += delta
                if src_p < target_p:
                    for p in range(src_p + 1, target_p + 1):
                        w = inv[p]
                        current_pos[w] -= 1
                        inv[p - 1] = w
                else:
                    for p in range(src_p - 1, target_p - 1, -1):
                        w = inv[p]
                        current_pos[w] += 1
                        inv[p + 1] = w
                current_pos[u] = target_p
                inv[target_p] = u

                if current_cost < best_cost:
                    best_cost = current_cost
                    best_pos = list(current_pos)
                    if best_cost <= B:
                        break

        T = max(T_min, T * decay)

    if best_cost <= B:
        print("YES")
        print(*(best_pos[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()