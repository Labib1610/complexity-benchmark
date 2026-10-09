import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    M = int(input_data[1])
    T = int(input_data[2])
    m = int(input_data[3])
    
    if n > M * T:
        print("NO")
        return
    
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)
    
    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        rev_adj[v].append(u)
        in_degree[v] += 1
        out_degree[u] += 1
        
    # Toposort to detect cycles and compute E (earliest day)
    q = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    topo_order = []
    E = [1] * (n + 1)
    
    in_deg_copy = list(in_degree)
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            if E[u] + 1 > E[v]:
                E[v] = E[u] + 1
            in_deg_copy[v] -= 1
            if in_deg_copy[v] == 0:
                q.append(v)
                
    if len(topo_order) < n:
        print("NO")
        return
    
    # Compute L (latest day)
    L = [T] * (n + 1)
    for u in reversed(topo_order):
        for v in adj[u]:
            if L[v] - 1 < L[u]:
                L[u] = L[v] - 1
                
    for i in range(1, n + 1):
        if E[i] > L[i] or E[i] > T or L[i] < 1:
            print("NO")
            return

    # Compute heights (longest path to sink)
    height = [0] * (n + 1)
    for u in reversed(topo_order):
        for v in adj[u]:
            if height[v] + 1 > height[u]:
                height[u] = height[v] + 1

    # Strategy 1: Forward list scheduling
    def try_forward():
        day_assignment = [0] * (n + 1)
        cur_in_deg = list(in_degree)
        available = [i for i in range(1, n + 1) if cur_in_deg[i] == 0]
        
        for d in range(1, T + 1):
            if not available:
                break
            # Sort available: lowest L[u] first, then highest height[u], then highest out_degree
            available.sort(key=lambda x: (L[x], -height[x], -out_degree[x]))
            
            # Check if any available has L[x] < d (impossible)
            for x in available:
                if L[x] < d:
                    return None
            
            pick = available[:M]
            available = available[M:]
            
            new_avail = []
            for u in pick:
                day_assignment[u] = d
                for v in adj[u]:
                    cur_in_deg[v] -= 1
                    if cur_in_deg[v] == 0:
                        new_avail.append(v)
            available.extend(new_avail)
            
        if all(day_assignment[i] > 0 for i in range(1, n + 1)):
            return day_assignment
        return None

    # Strategy 2: Backward list scheduling
    def try_backward():
        day_assignment = [0] * (n + 1)
        cur_out_deg = list(out_degree)
        available = [i for i in range(1, n + 1) if cur_out_deg[i] == 0]
        
        # Longest path from source
        depth = [0] * (n + 1)
        for u in topo_order:
            for v in adj[u]:
                if depth[u] + 1 > depth[v]:
                    depth[v] = depth[u] + 1
                    
        for d in range(T, 0, -1):
            if not available:
                break
            available.sort(key=lambda x: (-E[x], -depth[x], -in_degree[x]))
            
            for x in available:
                if E[x] > d:
                    return None
                    
            pick = available[:M]
            available = available[M:]
            
            new_avail = []
            for u in pick:
                day_assignment[u] = d
                for v in rev_adj[u]:
                    cur_out_deg[v] -= 1
                    if cur_out_deg[v] == 0:
                        new_avail.append(v)
            available.extend(new_avail)
            
        if all(day_assignment[i] > 0 for i in range(1, n + 1)):
            return day_assignment
        return None

    ans = try_forward()
    if ans is not None:
        print("YES")
        print(*(ans[1:]))
        return

    ans = try_backward()
    if ans is not None:
        print("YES")
        print(*(ans[1:]))
        return

    print("NO")

if __name__ == '__main__':
    solve()