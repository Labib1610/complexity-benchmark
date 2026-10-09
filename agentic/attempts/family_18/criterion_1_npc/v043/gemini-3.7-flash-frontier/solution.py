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
    adj = [[] for _ in range(n)]
    deg = [0] * n
    adj_mask = [0] * n
    
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
    if n <= 20:
        # Exact DP
        N = 1 << n
        cut = [0] * N
        for mask in range(1, N):
            v = (mask & -mask).bit_length() - 1
            prev = mask ^ (1 << v)
            # edges between v and prev:
            inter = bin(adj_mask[v] & prev).count('1')
            cut[mask] = cut[prev] + deg[v] - 2 * inter
            
        dp = [10**9] * N
        parent = [-1] * N
        dp[0] = 0
        
        for mask in range(N - 1):
            cur_d = dp[mask]
            if cur_d >= 10**9:
                continue
            c = cut[mask]
            # Try adding each unused vertex
            rem = ((N - 1) ^ mask)
            while rem:
                v = (rem & -rem).bit_length() - 1
                rem ^= (1 << v)
                nmask = mask | (1 << v)
                nd = cur_d + c
                if nd < dp[nmask]:
                    dp[nmask] = nd
                    parent[nmask] = v
                    
        total_cost = dp[N - 1]
        if total_cost > B:
            print("NO")
            return
            
        # Reconstruct
        order = []
        curr = N - 1
        while curr > 0:
            v = parent[curr]
            order.append(v)
            curr ^= (1 << v)
        order.reverse()
        
        bay = [0] * n
        for pos, mod in enumerate(order, 1):
            bay[mod] = pos
            
        print("YES")
        print(*(bay[i] for i in range(n)))
        return

    # For larger n, use Simulated Annealing / Local Search
    start_time = time.time()
    
    def compute_cost(perm):
        pos = [0] * n
        for p, u in enumerate(perm):
            pos[u] = p
        c = 0
        for u, v in edges:
            c += abs(pos[u] - pos[v])
        return c, pos

    # Initial order: greedy / degree-based
    best_perm = list(range(n))
    best_perm.sort(key=lambda x: -deg[x])
    best_cost, best_pos = compute_cost(best_perm)
    
    if best_cost <= B:
        bay = [0] * n
        for pos_idx, mod in enumerate(best_perm, 1):
            bay[mod] = pos_idx
        print("YES")
        print(*(bay[i] for i in range(n)))
        return

    current_perm = list(best_perm)
    current_cost = best_cost
    current_pos = list(best_pos)

    # SA parameters
    T_start = max(1.0, float(n))
    T_end = 0.01
    max_time = 4.5

    iter_count = 0
    while time.time() - start_time < max_time:
        iter_count += 1
        t_frac = (time.time() - start_time) / max_time
        T = T_start * ((T_end / T_start) ** t_frac)
        
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        if i == j:
            continue
        u = current_perm[i]
        v = current_perm[j]
        
        # Calculate delta cost of swapping i and j
        # Only edges incident to u and v change
        delta = 0
        for neighbor in adj[u]:
            if neighbor == v:
                continue
            p_nei = current_pos[neighbor]
            delta += abs(j - p_nei) - abs(i - p_nei)
        for neighbor in adj[v]:
            if neighbor == u:
                continue
            p_nei = current_pos[neighbor]
            delta += abs(i - p_nei) - abs(j - p_nei)
            
        if delta < 0 or random.random() < 2.718281828459045 ** (-delta / T):
            current_perm[i], current_perm[j] = current_perm[j], current_perm[i]
            current_pos[u] = j
            current_pos[v] = i
            current_cost += delta
            
            if current_cost < best_cost:
                best_cost = current_cost
                best_perm = list(current_perm)
                if best_cost <= B:
                    bay = [0] * n
                    for pos_idx, mod in enumerate(best_perm, 1):
                        bay[mod] = pos_idx
                    print("YES")
                    print(*(bay[i] for i in range(n)))
                    return

    if best_cost <= B:
        bay = [0] * n
        for pos_idx, mod in enumerate(best_perm, 1):
            bay[mod] = pos_idx
        print("YES")
        print(*(bay[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()