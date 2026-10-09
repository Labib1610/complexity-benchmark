import sys
import time

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    start_time = time.time()
    
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

    def compute_cost(order):
        pos = [0] * (n + 1)
        for p, node in enumerate(order, 1):
            pos[node] = p
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
        return cost, pos

    def get_layout(root):
        sz = [0] * (n + 1)
        tree_children = [[] for _ in range(n + 1)]
        
        stack = [(root, 0, 0)]
        order_dfs = []
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                order_dfs.append(u)
                stack.append((u, p, 1))
                for v in adj[u]:
                    if v != p:
                        tree_children[u].append(v)
                        stack.append((v, u, 0))
            else:
                s = 1
                for v in tree_children[u]:
                    s += sz[v]
                sz[u] = s

        def build_left(u):
            res = [u]
            ch = sorted(tree_children[u], key=lambda v: sz[v])
            for v in ch:
                res.extend(build_left(v))
            return res

        def build_right(u):
            res = []
            ch = sorted(tree_children[u], key=lambda v: -sz[v])
            for v in ch:
                res.extend(build_right(v))
            res.append(u)
            return res

        ch = tree_children[root]
        if not ch:
            return [root]
        
        total_sz = sum(sz[v] for v in ch)
        target = total_sz // 2
        
        dp = {0: []}
        for v in ch:
            s_v = sz[v]
            new_dp = dict(dp)
            for s, subset in dp.items():
                if s + s_v <= target and (s + s_v) not in new_dp:
                    new_dp[s + s_v] = subset + [v]
            dp = new_dp
            
        best_sum = max(dp.keys())
        left_set = set(dp[best_sum])
        
        L = [v for v in ch if v in left_set]
        R = [v for v in ch if v not in left_set]
        
        L.sort(key=lambda v: -sz[v])
        R.sort(key=lambda v: sz[v])
        
        res = []
        for v in L:
            res.extend(build_right(v))
        res.append(root)
        for v in R:
            res.extend(build_left(v))
        return res

    best_cost = float('inf')
    best_pos = None
    best_order = None

    roots = list(range(1, n + 1))
    if n > 500:
        degs = sorted(range(1, n + 1), key=lambda u: -len(adj[u]))
        roots = degs[:100] + list(range(1, min(n + 1, 100)))

    for r in roots:
        order = get_layout(r)
        cost, pos = compute_cost(order)
        if cost < best_cost:
            best_cost = cost
            best_pos = pos
            best_order = order
            if best_cost <= B:
                break
        if time.time() - start_time > 2.0:
            break

    # Simulated Annealing if budget not yet reached
    if best_cost > B and best_order is not None:
        import random
        cur_order = list(best_order)
        cur_pos = [0] * (n + 1)
        for i, u in enumerate(cur_order):
            cur_pos[u] = i
            
        cur_cost = best_cost
        T = 2.0
        decay = 0.99995
        
        while time.time() - start_time < 4.5:
            i = random.randint(0, n - 2)
            u = cur_order[i]
            v = cur_order[i + 1]
            
            delta = 0
            for w in adj[u]:
                if w != v:
                    old_d = abs(i - cur_pos[w])
                    new_d = abs(i + 1 - cur_pos[w])
                    delta += (new_d - old_d)
            for w in adj[v]:
                if w != u:
                    old_d = abs(i + 1 - cur_pos[w])
                    new_d = abs(i - cur_pos[w])
                    delta += (new_d - old_d)
            
            if delta <= 0 or (T > 1e-4 and random.random() < pow(2.71828, -delta / T)):
                cur_cost += delta
                cur_order[i], cur_order[i + 1] = cur_order[i + 1], cur_order[i]
                cur_pos[u] = i + 1
                cur_pos[v] = i
                
                if cur_cost < best_cost:
                    best_cost = cur_cost
                    best_pos = [p + 1 for p in cur_pos]
                    if best_cost <= B:
                        break
            
            T *= decay

    if best_cost <= B:
        print("YES")
        print(*(best_pos[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()