import sys
import time
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
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        idx += 2

    def get_layout(root):
        parent = [0] * (n + 1)
        children = [[] for _ in range(n + 1)]
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
        
        sz = [1] * (n + 1)
        for u in reversed(order):
            for v in children[u]:
                sz[u] += sz[v]
        
        def build(u, bias):
            ch = children[u]
            if not ch:
                return [u]
            
            if bias == 'left':
                ch_sorted = sorted(ch, key=lambda c: sz[c])
                res = [u]
                for c in ch_sorted:
                    res.extend(build(c, 'left'))
                return res
            elif bias == 'right':
                ch_sorted = sorted(ch, key=lambda c: -sz[c])
                res = []
                for c in ch_sorted:
                    res.extend(build(c, 'right'))
                res.append(u)
                return res
            else:
                total = sz[u] - 1
                target = total // 2
                
                dp = {0: []}
                for c in ch:
                    c_sz = sz[c]
                    for w in sorted(dp.keys(), reverse=True):
                        if w + c_sz <= target and (w + c_sz) not in dp:
                            dp[w + c_sz] = dp[w] + [c]
                
                best_w = max(dp.keys())
                left_set = set(dp[best_w])
                
                left_ch = [c for c in ch if c in left_set]
                right_ch = [c for c in ch if c not in left_set]
                
                left_ch.sort(key=lambda c: -sz[c])
                right_ch.sort(key=lambda c: sz[c])
                
                res = []
                for c in left_ch:
                    res.extend(build(c, 'right'))
                res.append(u)
                for c in right_ch:
                    res.extend(build(c, 'left'))
                return res

        return build(root, 'center')

    def compute_cost(arr):
        pos = [0] * (n + 1)
        for i, u in enumerate(arr):
            pos[u] = i
        cost = sum(abs(pos[u] - pos[v]) for u, v in edges)
        return cost, pos

    best_cost = float('inf')
    best_arr = None

    roots = list(range(1, n + 1))
    roots.sort(key=lambda u: -len(adj[u]))
    
    if len(roots) > 300:
        roots = roots[:150] + random.sample(roots[150:], min(150, len(roots) - 150))
    
    for r in roots:
        arr = get_layout(r)
        cost, _ = compute_cost(arr)
        if cost < best_cost:
            best_cost = cost
            best_arr = arr
            if best_cost <= B:
                break
        if time.time() - start_time > 2.0:
            break

    if best_cost > B:
        arr = list(best_arr)
        pos = [0] * (n + 1)
        for i, u in enumerate(arr):
            pos[u] = i
        current_cost = best_cost

        T = 1.0
        decay = 0.9995
        steps = 0
        
        while time.time() - start_time < 4.5:
            improved = False
            for k in range(n - 1):
                u = arr[k]
                v = arr[k + 1]
                
                L_u = 0
                deg_prime_u = 0
                for w in adj[u]:
                    if w == v:
                        continue
                    deg_prime_u += 1
                    if pos[w] < k:
                        L_u += 1
                
                L_v = 0
                deg_prime_v = 0
                for w in adj[v]:
                    if w == u:
                        continue
                    deg_prime_v += 1
                    if pos[w] < k:
                        L_v += 1
                
                delta = (2 * L_u - deg_prime_u) - (2 * L_v - deg_prime_v)
                
                if delta < 0 or (T > 1e-4 and random.random() < pow(2.718281828, -delta / max(T, 1e-4))):
                    arr[k], arr[k + 1] = v, u
                    pos[u] = k + 1
                    pos[v] = k
                    current_cost += delta
                    if delta < 0:
                        improved = True
                    
                    if current_cost < best_cost:
                        best_cost = current_cost
                        best_arr = list(arr)
                        if best_cost <= B:
                            break
            
            if best_cost <= B:
                break
            
            T *= decay
            steps += 1

    if best_cost <= B:
        print("YES")
        slot = [0] * (n + 1)
        for i, u in enumerate(best_arr):
            slot[u] = i + 1
        print(*(slot[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()