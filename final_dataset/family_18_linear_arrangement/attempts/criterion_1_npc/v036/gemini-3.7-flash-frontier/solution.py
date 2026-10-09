import sys
import random
import time

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    adj = [[] for _ in range(n)]
    adj_mask = [0] * n
    edges = []
    
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        edges.append((u, v))
        
    deg = [len(adj[i]) for i in range(n)]

    # If n is small, exact DP is feasible and guaranteed optimal
    if n <= 20:
        total_states = 1 << n
        cut = [0] * total_states
        
        for mask in range(1, total_states):
            lsb = mask & -mask
            u = lsb.bit_length() - 1
            prev = mask ^ lsb
            cut[mask] = cut[prev] + deg[u] - 2 * (adj_mask[u] & prev).bit_count()
            
        INF = 10**15
        dp = [INF] * total_states
        parent = [-1] * total_states
        dp[0] = 0
        
        for mask in range(total_states - 1):
            cur_cost = dp[mask] + cut[mask]
            rem = (total_states - 1) ^ mask
            while rem:
                lsb = rem & -rem
                nxt = mask | lsb
                if cur_cost < dp[nxt]:
                    dp[nxt] = cur_cost
                    parent[nxt] = lsb.bit_length() - 1
                rem ^= lsb
                
        if dp[total_states - 1] > B:
            print("NO")
            return
        
        # Reconstruct sequence of instruments
        order = []
        curr = total_states - 1
        while curr > 0:
            u = parent[curr]
            order.append(u)
            curr ^= (1 << u)
        order.reverse()
        
        # bracket_assignment[k] = bracket of instrument k
        ans = [0] * n
        for bracket, inst in enumerate(order, 1):
            ans[inst] = bracket
            
        print("YES")
        print(*(ans))
        return

    # For larger n, use Simulated Annealing / Local Search
    def compute_cost(pos):
        c = 0
        for u, v in edges:
            c += abs(pos[u] - pos[v])
        return c

    start_time = time.time()
    
    # Greedy ordering using BFS/Cuthill-McKee heuristic
    visited = [False] * n
    initial_order = []
    
    # Start with smallest degree
    nodes_by_deg = sorted(range(n), key=lambda x: deg[x])
    for start_node in nodes_by_deg:
        if not visited[start_node]:
            queue = [start_node]
            visited[start_node] = True
            while queue:
                u = queue.pop(0)
                initial_order.append(u)
                neighbors = sorted(adj[u], key=lambda x: deg[x])
                for v in neighbors:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
                        
    order = list(initial_order)
    pos = [0] * n
    for i, u in enumerate(order):
        pos[u] = i + 1
        
    best_cost = compute_cost(pos)
    best_pos = list(pos)
    
    if best_cost <= B:
        print("YES")
        print(*best_pos)
        return

    # Simulated Annealing
    T_start = 50.0
    T_end = 0.01
    max_time = 4.5
    
    cur_cost = best_cost
    steps = 0
    
    while time.time() - start_time < max_time:
        steps += 1
        T = T_start * ((T_end / T_start) ** ((time.time() - start_time) / max_time))
        
        # Pick two indices in order to swap
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        if i == j:
            continue
            
        u, v = order[i], order[j]
        
        # Compute delta
        delta = 0
        for w in adj[u]:
            if w != v:
                delta += abs(j + 1 - pos[w]) - abs(i + 1 - pos[w])
        for w in adj[v]:
            if w != u:
                delta += abs(i + 1 - pos[w]) - abs(j + 1 - pos[w])
                
        if delta < 0 or (T > 0 and random.random() < 2.718281828459045 ** (-delta / T)):
            order[i], order[j] = v, u
            pos[u] = j + 1
            pos[v] = i + 1
            cur_cost += delta
            
            if cur_cost < best_cost:
                best_cost = cur_cost
                best_pos = list(pos)
                if best_cost <= B:
                    print("YES")
                    print(*best_pos)
                    return

    if best_cost <= B:
        print("YES")
        print(*best_pos)
    else:
        print("NO")

if __name__ == '__main__':
    solve()