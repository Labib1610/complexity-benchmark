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
    
    adj_list = [[] for _ in range(n)]
    adj_mask = [0] * n
    deg = [0] * n
    
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v:
            adj_list[u].append(v)
            adj_list[v].append(u)
            adj_mask[u] |= (1 << v)
            adj_mask[v] |= (1 << u)
            deg[u] += 1
            deg[v] += 1

    if n <= 21:
        # Exact DP
        size = 1 << n
        dp = [0] * size
        parent = [0] * size
        cut = [0] * size
        
        for mask in range(1, size):
            lsb = mask & -mask
            u = (lsb).bit_length() - 1
            prev_mask = mask ^ lsb
            cut[mask] = cut[prev_mask] + deg[u] - 2 * (adj_mask[u] & prev_mask).bit_count()
            
            # Find min over all u in mask
            min_val = float('inf')
            best_u = -1
            
            temp = mask
            while temp:
                bit = temp & -temp
                v = bit.bit_length() - 1
                val = dp[mask ^ bit]
                if val < min_val:
                    min_val = val
                    best_u = v
                temp ^= bit
            
            dp[mask] = min_val + cut[mask]
            parent[mask] = best_u
            
        final_cost = dp[(1 << n) - 1]
        if final_cost > B:
            print("NO")
            return
        
        # Reconstruct order of placement from position n down to 1
        order = []
        curr = (1 << n) - 1
        while curr > 0:
            u = parent[curr]
            order.append(u)
            curr ^= (1 << u)
        
        order.reverse()
        # order[i] is the module placed at bay (i + 1)
        pos = [0] * n
        for bay_idx, mod in enumerate(order):
            pos[mod] = bay_idx + 1
            
        print("YES")
        print(*(pos[i] for i in range(n)))
        return

    # For larger n, use Simulated Annealing
    start_time = time.time()
    
    def compute_cost(p):
        # p is list where p[bay] = module
        # module_pos[mod] = bay
        mod_pos = [0] * n
        for i, mod in enumerate(p):
            mod_pos[mod] = i
        total = 0
        for u in range(n):
            for v in adj_list[u]:
                if u < v:
                    total += abs(mod_pos[u] - mod_pos[v])
        return total, mod_pos

    # Initial solution: BFS/degree heuristic or random
    best_p = list(range(n))
    best_cost, best_pos = compute_cost(best_p)
    if best_cost <= B:
        print("YES")
        print(*(best_pos[i] + 1 for i in range(n)))
        return

    # SA loop
    curr_p = list(best_p)
    curr_cost = best_cost
    pos_arr = [0] * n
    for i, mod in enumerate(curr_p):
        pos_arr[mod] = i
        
    T = 100.0
    T_min = 1e-3
    alpha = 0.99995

    while time.time() - start_time < 4.5:
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        if i == j:
            continue
        
        u = curr_p[i]
        v = curr_p[j]
        
        # Delta cost calculation
        delta = 0
        for nbr in adj_list[u]:
            if nbr != v:
                nbr_pos = pos_arr[nbr]
                delta += abs(j - nbr_pos) - abs(i - nbr_pos)
        for nbr in adj_list[v]:
            if nbr != u:
                nbr_pos = pos_arr[nbr]
                delta += abs(i - nbr_pos) - abs(j - nbr_pos)
                
        if delta < 0 or (T > 0 and random.random() < pow(2.718281828459045, -delta / T)):
            curr_p[i], curr_p[j] = curr_p[j], curr_p[i]
            pos_arr[u], pos_arr[v] = j, i
            curr_cost += delta
            if curr_cost < best_cost:
                best_cost = curr_cost
                if best_cost <= B:
                    print("YES")
                    ans_pos = [0] * n
                    for bay, mod in enumerate(curr_p):
                        ans_pos[mod] = bay + 1
                    print(*(ans_pos[k] for k in range(n)))
                    return
        T = max(T_min, T * alpha)

    if best_cost <= B:
        print("YES")
        ans_pos = [0] * n
        for bay, mod in enumerate(curr_p):
            ans_pos[mod] = bay + 1
        print(*(ans_pos[k] for k in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()