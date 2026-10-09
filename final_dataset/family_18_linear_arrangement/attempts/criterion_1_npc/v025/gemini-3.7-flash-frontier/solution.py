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
    
    edges = []
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        edges.append((u, v))
        idx += 2

    # Check identity permutation first
    id_cost = sum(abs(u - v) for u, v in edges)
    if id_cost <= B:
        print("YES")
        print(*(i + 1 for i in range(n)))
        return

    # Check reverse permutation
    rev_cost = sum(abs((n - 1 - u) - (n - 1 - v)) for u, v in edges)
    if rev_cost <= B:
        print("YES")
        print(*(n - i for i in range(n)))
        return

    # Small n: exact DP (Optimal Linear Arrangement)
    if n <= 14:
        adj_mask = [0] * n
        deg = [0] * n
        for u, v in edges:
            adj_mask[u] |= (1 << v)
            adj_mask[v] |= (1 << u)
            deg[u] += 1
            deg[v] += 1
            
        num_masks = 1 << n
        cut = [0] * num_masks
        for mask in range(1, num_masks):
            # lowest set bit
            lsb = mask & -mask
            v = lsb.bit_length() - 1
            prev_mask = mask ^ lsb
            edges_to_prev = (prev_mask & adj_mask[v]).bit_count()
            cut[mask] = cut[prev_mask] + deg[v] - 2 * edges_to_prev
            
        INF = float('inf')
        dp = [INF] * num_masks
        parent = [-1] * num_masks
        dp[0] = 0
        
        for mask in range(num_masks - 1):
            cur_dp = dp[mask]
            if cur_dp == INF:
                continue
            for v in range(n):
                if not (mask & (1 << v)):
                    nmask = mask | (1 << v)
                    cost = cur_dp + cut[nmask]
                    if cost < dp[nmask]:
                        dp[nmask] = cost
                        parent[nmask] = v
                        
        if dp[num_masks - 1] <= B:
            # Reconstruct
            order = []
            curr = num_masks - 1
            while curr > 0:
                v = parent[curr]
                order.append(v)
                curr ^= (1 << v)
            order.reverse()
            
            p = [0] * n
            for slot, v in enumerate(order, 1):
                p[v] = slot
            print("YES")
            print(*p)
            return
        else:
            print("NO")
            return

    # Heuristic / Local search for larger n
    start_time = time.time()
    
    # Adjacency list for fast evaluation
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def compute_cost(pos):
        return sum(abs(pos[u] - pos[v]) for u, v in edges)

    best_p = list(range(n))
    best_cost = id_cost

    # Try sorting by degree as an initial state
    deg_order = sorted(range(n), key=lambda x: len(adj[x]), reverse=True)
    pos = [0] * n
    for slot, v in enumerate(deg_order):
        pos[v] = slot
    cost = compute_cost(pos)
    if cost <= B:
        print("YES")
        print(*(pos[i] + 1 for i in range(n)))
        return

    # Simulated Annealing / Hill Climbing
    current_order = list(range(n))
    pos = list(range(n))
    cur_cost = id_cost

    # Temperature
    T = 100.0
    decay = 0.9995

    while time.time() - start_time < 4.0:
        # Pick two random slots to swap
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        if i == j:
            continue
        
        u = current_order[i]
        v = current_order[j]

        # Calculate delta cost of swapping u at i and v at j
        delta = 0
        for neighbor in adj[u]:
            if neighbor != v:
                delta += abs(j - pos[neighbor]) - abs(i - pos[neighbor])
        for neighbor in adj[v]:
            if neighbor != u:
                delta += abs(i - pos[neighbor]) - abs(j - pos[neighbor])

        if delta < 0 or (T > 1e-4 and random.random() < 2.71828 ** (-delta / T)):
            cur_cost += delta
            current_order[i], current_order[j] = v, u
            pos[u], pos[v] = j, i
            if cur_cost < best_cost:
                best_cost = cur_cost
                if best_cost <= B:
                    print("YES")
                    print(*(pos[k] + 1 for k in range(n)))
                    return

        T *= decay
        if T < 1e-3:
            T = 50.0

    print("NO")

if __name__ == '__main__':
    solve()