import sys
import time
import math
import random

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    start_time = time.time()
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    if n == 1:
        print("YES")
        print("1")
        return
        
    adj = [[] for _ in range(n + 1)]
    idx = 3
    edges = []
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    def compute_cost(pos):
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
        return cost

    best_cost = float('inf')
    best_pos = None

    def update_best(pos):
        nonlocal best_cost, best_pos
        c = compute_cost(pos)
        if c < best_cost:
            best_cost = c
            best_pos = list(pos)
        return c

    # Heuristic 1: Contiguous Tree Placement
    def build_from_root(root):
        parent = [0] * (n + 1)
        children = [[] for _ in range(n + 1)]
        sz = [1] * (n + 1)
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
                    children[u].append(v)
                    stack.append(v)
                    
        for u in reversed(order):
            for v in children[u]:
                sz[u] += sz[v]
                
        def get_seq(u, side):
            # side: 'L' means u should be at the right boundary
            # 'R' means u should be at the left boundary
            # 'M' means u is root, children split left and right
            ch = children[u]
            if not ch:
                return [u]
            
            if side == 'M':
                # split children into left and right
                ch_sorted = sorted(ch, key=lambda x: sz[x], reverse=True)
                left_ch, right_ch = [], []
                sz_l, sz_r = 0, 0
                for c in ch_sorted:
                    if sz_l <= sz_r:
                        left_ch.append(c)
                        sz_l += sz[c]
                    else:
                        right_ch.append(c)
                        sz_r += sz[c]
                
                left_ch.sort(key=lambda x: sz[x])
                right_ch.sort(key=lambda x: sz[x], reverse=True)
                
                res = []
                for c in left_ch:
                    res.extend(get_seq(c, 'L'))
                res.append(u)
                for c in right_ch:
                    res.extend(get_seq(c, 'R'))
                return res
            
            elif side == 'L':
                # u at right boundary
                ch_sorted = sorted(ch, key=lambda x: sz[x])
                res = []
                for c in ch_sorted:
                    res.extend(get_seq(c, 'L'))
                res.append(u)
                return res
            else:
                # u at left boundary
                ch_sorted = sorted(ch, key=lambda x: sz[x], reverse=True)
                res = [u]
                for c in ch_sorted:
                    res.extend(get_seq(c, 'R'))
                return res

        arr = get_seq(root, 'M')
        pos = [0] * (n + 1)
        for i, u in enumerate(arr):
            pos[u] = i + 1
        return pos

    # Evaluate tree rootings
    deg = [len(adj[i]) for i in range(n + 1)]
    candidates = sorted(range(1, n + 1), key=lambda x: deg[x], reverse=True)
    
    num_roots = min(n, 40)
    for r in candidates[:num_roots]:
        pos = build_from_root(r)
        if update_best(pos) <= B:
            print("YES")
            print(*(best_pos[1:]))
            return

    # Heuristic 2: Spectral Ordering (Fiedler Vector via Power Iteration)
    if n > 2:
        max_deg = max(deg[1:])
        x = [math.sin(i * 1.5) for i in range(n + 1)]
        x[0] = 0
        
        for _ in range(150):
            mean = sum(x[1:]) / n
            for i in range(1, n + 1):
                x[i] -= mean
            
            norm = math.sqrt(sum(x[i]**2 for i in range(1, n + 1)))
            if norm > 1e-9:
                for i in range(1, n + 1):
                    x[i] /= norm
            
            nx = [0.0] * (n + 1)
            for u in range(1, n + 1):
                s = sum(x[v] for v in adj[u])
                nx[u] = (max_deg + 1 - deg[u]) * x[u] + s
            x = nx
            
        nodes = sorted(range(1, n + 1), key=lambda u: x[u])
        pos_spec = [0] * (n + 1)
        for i, u in enumerate(nodes):
            pos_spec[u] = i + 1
        if update_best(pos_spec) <= B:
            print("YES")
            print(*(best_pos[1:]))
            return

    # Heuristic 3: Simulated Annealing
    cur_pos = list(best_pos)
    cur_slot = [0] * (n + 1) # slot[p] = node at position p
    for u in range(1, n + 1):
        cur_slot[cur_pos[u]] = u

    cur_cost = best_cost

    # Pre-build edge pairs for fast delta calculation
    adj_no_self = [list(adj[u]) for u in range(n + 1)]

    def get_swap_delta(u, v, pos_u, pos_v):
        delta = 0
        for w in adj_no_self[u]:
            if w != v:
                pos_w = cur_pos[w]
                delta += abs(pos_v - pos_w) - abs(pos_u - pos_w)
        for w in adj_no_self[v]:
            if w != u:
                pos_w = cur_pos[w]
                delta += abs(pos_u - pos_w) - abs(pos_v - pos_w)
        return delta

    T_start = 2.0
    T_end = 0.01
    max_time = 4.3

    iter_count = 0
    while time.time() - start_time < max_time:
        iter_count += 1
        fraction = (time.time() - start_time) / max_time
        T = T_start * ((T_end / T_start) ** fraction)
        
        # Choose two positions to swap
        # Bias towards closer positions for fine-tuning, with occasional long jumps
        p1 = random.randint(1, n)
        if random.random() < 0.7:
            offset = int(random.gauss(0, max(1, n * 0.05)))
            p2 = p1 + offset
            if p2 < 1 or p2 > n or p2 == p1:
                p2 = random.randint(1, n)
        else:
            p2 = random.randint(1, n)
            
        if p1 == p2:
            continue
            
        u = cur_slot[p1]
        v = cur_slot[p2]
        
        delta = get_swap_delta(u, v, p1, p2)
        
        if delta < 0 or (T > 1e-6 and math.exp(-delta / T) > random.random()):
            cur_pos[u] = p2
            cur_pos[v] = p1
            cur_slot[p1] = v
            cur_slot[p2] = u
            cur_cost += delta
            
            if cur_cost < best_cost:
                best_cost = cur_cost
                best_pos = list(cur_pos)
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