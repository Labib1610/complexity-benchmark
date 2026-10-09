import sys
import random
import time
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
            print("1")
        else:
            print("NO")
        return

    adj = [[] for _ in range(n)]
    edge_set = set()
    
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        if u > v:
            u, v = v, u
        edge_set.add((u, v))
        
    start_time = time.time()
    
    # 1. Fiedler vector ordering
    max_d = max(len(adj[i]) for i in range(n))
    shift = 2 * max_d + 1
    
    random.seed(42)
    x = [random.gauss(0, 1) for _ in range(n)]
    mean_x = sum(x) / n
    x = [val - mean_x for val in x]
    
    for _ in range(40):
        y = [0.0] * n
        for u in range(n):
            s = (shift - len(adj[u])) * x[u]
            for v in adj[u]:
                s += x[v]
            y[u] = s
        mean_y = sum(y) / n
        norm_y = math.sqrt(sum((val - mean_y) ** 2 for val in y))
        if norm_y < 1e-9:
            break
        x = [(val - mean_y) / norm_y for val in y]
        
    order = sorted(range(n), key=lambda i: x[i])
    
    # Setup initial state
    pos = [0] * n
    for p, u in enumerate(order):
        pos[u] = p
        
    left_deg = [0] * n
    right_deg = [0] * n
    total_friction = 0
    
    for u in range(n):
        pu = pos[u]
        for v in adj[u]:
            pv = pos[v]
            if pv < pu:
                left_deg[u] += 1
            else:
                right_deg[u] += 1
            if u < v:
                total_friction += abs(pu - pv)
                
    if total_friction <= B:
        print("YES")
        ans = [0] * n
        for u in range(n):
            ans[u] = pos[u] + 1
        print(*(ans))
        return

    # Local search with Simulated Annealing
    T = 1.0
    cooling_rate = 0.99995
    min_T = 1e-4
    
    best_friction = total_friction
    best_pos = list(pos)
    
    step = 0
    while time.time() - start_time < 4.5:
        step += 1
        # Sweep passes
        improved = False
        for i in range(n - 1):
            u = order[i]
            v = order[i + 1]
            
            is_adj = 1 if (u < v and (u, v) in edge_set) or (v < u and (v, u) in edge_set) else 0
            delta = (left_deg[u] - right_deg[u]) - (left_deg[v] - right_deg[v]) + 2 * is_adj
            
            if delta <= 0 or (T > min_T and math.exp(-delta / T) > random.random()):
                # Apply swap
                order[i], order[i + 1] = v, u
                pos[u] = i + 1
                pos[v] = i
                
                left_deg[u] += is_adj
                right_deg[u] -= is_adj
                left_deg[v] -= is_adj
                right_deg[v] += is_adj
                
                total_friction += delta
                if delta < 0:
                    improved = True
                
                if total_friction < best_friction:
                    best_friction = total_friction
                    best_pos = list(pos)
                    if best_friction <= B:
                        print("YES")
                        ans = [best_pos[u] + 1 for u in range(n)]
                        print(*(ans))
                        return
                        
        T = max(min_T, T * cooling_rate)
        if not improved and T <= min_T:
            # Reheat
            T = 0.5
            
    if best_friction <= B:
        print("YES")
        ans = [best_pos[u] + 1 for u in range(n)]
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()