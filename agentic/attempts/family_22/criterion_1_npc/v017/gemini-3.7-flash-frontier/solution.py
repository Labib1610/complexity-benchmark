import sys
from collections import deque
import random

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
    radj = [[] for _ in range(n + 1)]
    in_deg = [0] * (n + 1)
    out_deg = [0] * (n + 1)
    
    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        radj[v].append(u)
        in_deg[v] += 1
        out_deg[u] += 1

    # Topological sort & cycle check
    q = deque([i for i in range(1, n + 1) if in_deg[i] == 0])
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                q.append(v)
                
    if len(topo_order) < n:
        print("NO")
        return

    # Earliest start (ES)
    es = [1] * (n + 1)
    for u in topo_order:
        for v in adj[u]:
            if es[u] + 1 > es[v]:
                es[v] = es[u] + 1

    # Latest start (LS)
    ls = [T] * (n + 1)
    for u in reversed(topo_order):
        for v in adj[u]:
            if ls[v] - 1 < ls[u]:
                ls[u] = ls[v] - 1

    for i in range(1, n + 1):
        if es[i] > ls[i]:
            print("NO")
            return

    # Critical path length / depth for tie breaking
    depth = [0] * (n + 1)
    for u in reversed(topo_order):
        d = 0
        for v in adj[u]:
            if depth[v] + 1 > d:
                d = depth[v] + 1
        depth[u] = d

    # Heuristic 1: Forward list scheduling with Earliest Deadline First (EDF)
    def try_forward(weights=None):
        assigned_cycle = [0] * (n + 1)
        pred_count = [len(radj[i]) for i in range(n + 1)]
        ready = [i for i in range(1, n + 1) if pred_count[i] == 0]
        
        for t in range(1, T + 1):
            if not ready:
                break
            # Filter ready jobs that can be scheduled at time t
            # Sort ready by: ls[i], -depth[i], random perturbation if weights
            if weights:
                ready.sort(key=lambda x: (ls[x], -depth[x], weights[x]))
            else:
                ready.sort(key=lambda x: (ls[x], -depth[x]))
            
            # Select up to M
            chosen = ready[:M]
            ready = ready[M:]
            
            for u in chosen:
                assigned_cycle[u] = t
                for v in adj[u]:
                    pred_count[v] -= 1
                    if pred_count[v] == 0:
                        ready.append(v)
                        
        if all(assigned_cycle[i] > 0 for i in range(1, n + 1)):
            return assigned_cycle
        return None

    # Heuristic 2: Backward list scheduling
    def try_backward(weights=None):
        assigned_cycle = [0] * (n + 1)
        succ_count = [len(adj[i]) for i in range(n + 1)]
        ready = [i for i in range(1, n + 1) if succ_count[i] == 0]
        
        for t in range(T, 0, -1):
            if not ready:
                break
            if weights:
                ready.sort(key=lambda x: (-es[x], depth[x], weights[x]))
            else:
                ready.sort(key=lambda x: (-es[x], depth[x]))
            
            chosen = ready[:M]
            ready = ready[M:]
            
            for u in chosen:
                assigned_cycle[u] = t
                for p in radj[u]:
                    succ_count[p] -= 1
                    if succ_count[p] == 0:
                        ready.append(p)
                        
        if all(assigned_cycle[i] > 0 for i in range(1, n + 1)):
            return assigned_cycle
        return None

    res = try_forward()
    if res:
        print("YES")
        print(*(res[1:]))
        return

    res = try_backward()
    if res:
        print("YES")
        print(*(res[1:]))
        return

    # Randomized trials
    rng = random.Random(42)
    for _ in range(500):
        weights = [rng.random() for _ in range(n + 1)]
        res = try_forward(weights)
        if res:
            print("YES")
            print(*(res[1:]))
            return
        res = try_backward(weights)
        if res:
            print("YES")
            print(*(res[1:]))
            return

    # Backtracking search
    # Try cycle-by-cycle branch and bound if search space is small
    assigned = [0] * (n + 1)
    pred_left = [len(radj[i]) for i in range(n + 1)]
    
    def backtrack(t, cur_ready):
        if all(assigned[i] > 0 for i in range(1, n + 1)):
            return True
        if t > T:
            return False
        
        # Mandatory jobs that must be scheduled at or before t
        must_schedule = [u for u in cur_ready if ls[u] == t]
        if len(must_schedule) > M:
            return False
        
        # Sort ready jobs
        cur_ready.sort(key=lambda x: (ls[x], -depth[x]))
        
        # Try different subsets of size up to M
        from itertools import combinations
        rem_slots = M - len(must_schedule)
        other_ready = [u for u in cur_ready if ls[u] > t]
        
        if len(other_ready) <= rem_slots:
            subsets = [must_schedule + other_ready]
        else:
            # Pick greedy subset first, then others
            subsets = [must_schedule + other_ready[:rem_slots]]
            # Add a few alternatives
            for combo in combinations(other_ready[:min(rem_slots + 3, len(other_ready))], rem_slots):
                candidate = must_schedule + list(combo)
                if candidate not in subsets:
                    subsets.append(candidate)
                    if len(subsets) >= 10:
                        break

        for chosen in subsets:
            next_ready = [u for u in cur_ready if u not in chosen]
            for u in chosen:
                assigned[u] = t
                for v in adj[u]:
                    pred_left[v] -= 1
                    if pred_left[v] == 0:
                        next_ready.append(v)
            
            if backtrack(t + 1, next_ready):
                return True
            
            for u in chosen:
                assigned[u] = 0
                for v in adj[u]:
                    pred_left[v] += 1

        return False

    initial_ready = [i for i in range(1, n + 1) if pred_left[i] == 0]
    if backtrack(1, initial_ready):
        print("YES")
        print(*(assigned[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()