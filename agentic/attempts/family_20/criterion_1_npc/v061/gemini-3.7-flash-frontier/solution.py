import sys
import random
import time

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
        
    # Check degree: all must be 3
    for i in range(1, n + 1):
        if len(adj[i]) != 3:
            print("NO")
            return

    start_time = time.time()
    time_limit = 4.5  # seconds

    # We use Kempe chain / local search / backtracking
    # Let's use a hybrid approach:
    # 1. Backtracking with MRV and degree heuristic (very fast on most instances)
    # 2. If it takes too many backtracks, fall back to min-conflicts local search.

    # Fast Backtracking with forward checking
    edge_color = [-1] * m
    # vertex_used_colors[v] bitmask of used colors (1: bit 0, 2: bit 1, 3: bit 2)
    vertex_mask = [0] * (n + 1)
    
    # Sort edges by degrees or simply process
    # To optimize backtracking:
    order = list(range(m))
    # Order edges to form a connected component / spanning tree first
    visited_v = [False] * (n + 1)
    visited_e = [False] * m
    bfs_order = []
    for start_node in range(1, n + 1):
        if visited_v[start_node]:
            continue
        queue = [start_node]
        visited_v[start_node] = True
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1
            for e_idx in adj[curr]:
                if not visited_e[e_idx]:
                    visited_e[e_idx] = True
                    bfs_order.append(e_idx)
                    u, v = edges[e_idx]
                    nxt = v if u == curr else u
                    if not visited_v[nxt]:
                        visited_v[nxt] = True
                        queue.append(nxt)

    order = bfs_order

    found = False
    max_nodes = 400000
    nodes_count = 0

    def backtrack(idx_in_order):
        nonlocal nodes_count, found
        nodes_count += 1
        if nodes_count > max_nodes:
            return False
        if idx_in_order == m:
            found = True
            return True

        e_idx = order[idx_in_order]
        u, v = edges[e_idx]
        avail = 7 & ~(vertex_mask[u] | vertex_mask[v])
        
        if not avail:
            return False

        # Try colors
        # Randomize color order slightly or fixed
        colors = []
        if avail & 1: colors.append(0)
        if avail & 2: colors.append(1)
        if avail & 4: colors.append(2)

        for c in colors:
            bit = 1 << c
            vertex_mask[u] |= bit
            vertex_mask[v] |= bit
            edge_color[e_idx] = c + 1

            if backtrack(idx_in_order + 1):
                return True

            vertex_mask[u] &= ~bit
            vertex_mask[v] &= ~bit
            edge_color[e_idx] = -1

        return False

    if backtrack(0):
        print("YES")
        print(*(edge_color))
        return

    # If backtracking failed due to limit, let's use Min-Conflicts Local Search
    # Initialize data structures for Min-Conflicts
    while time.time() - start_time < time_limit:
        color = [random.randint(1, 3) for _ in range(m)]
        # count_col[v][c] = number of incident edges with color c
        count_col = [[0] * 4 for _ in range(n + 1)]
        for i in range(m):
            u, v = edges[i]
            c = color[i]
            count_col[u][c] += 1
            count_col[v][c] += 1

        # Conflicted edges
        conflicts = 0
        for v in range(1, n + 1):
            for c in (1, 2, 3):
                if count_col[v][c] > 1:
                    conflicts += count_col[v][c] - 1

        if conflicts == 0:
            print("YES")
            print(*(color))
            return

        # Local search iterations
        max_steps = 150000
        for step in range(max_steps):
            if step % 2000 == 0 and time.time() - start_time >= time_limit:
                break

            # Pick a random edge
            e_idx = random.randint(0, m - 1)
            u, v = edges[e_idx]
            cur_c = color[e_idx]

            # Check if this edge is in conflict
            if count_col[u][cur_c] <= 1 and count_col[v][cur_c] <= 1:
                # Random walk with small probability
                if random.random() > 0.05:
                    continue

            # Evaluate cost change for colors 1, 2, 3
            best_c = cur_c
            best_delta = 0

            # Current contribution of u and v for cur_c:
            # removing cur_c decreases conflict if count > 1
            delta_remove = 0
            if count_col[u][cur_c] > 1:
                delta_remove -= 1
            if count_col[v][cur_c] > 1:
                delta_remove -= 1

            candidates = []
            min_d = 100

            for nc in (1, 2, 3):
                if nc == cur_c:
                    d = 0
                else:
                    d = delta_remove
                    if count_col[u][nc] >= 1:
                        d += 1
                    if count_col[v][nc] >= 1:
                        d += 1

                if d < min_d:
                    min_d = d
                    candidates = [nc]
                elif d == min_d:
                    candidates.append(nc)

            best_c = random.choice(candidates)

            if best_c != cur_c:
                count_col[u][cur_c] -= 1
                count_col[v][cur_c] -= 1
                count_col[u][best_c] += 1
                count_col[v][best_c] += 1
                color[e_idx] = best_c
                conflicts += min_d

                if conflicts == 0:
                    print("YES")
                    print(*(color))
                    return

    print("NO")

if __name__ == '__main__':
    solve()