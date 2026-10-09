import sys
from collections import deque
import itertools

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    M = int(input_data[1])
    T = int(input_data[2])
    m = int(input_data[3])
    
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)
    
    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        rev_adj[v].append(u)
        in_degree[v] += 1
        out_degree[u] += 1
        
    # Check for cycles / Topological sort
    q = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
                
    if len(topo) < n:
        print("NO")
        return

    # Compute E[u] (earliest start time, 1-indexed)
    E = [1] * (n + 1)
    for u in topo:
        for v in adj[u]:
            if E[u] + 1 > E[v]:
                E[v] = E[u] + 1

    # Compute L[u] (latest start time, 1-indexed)
    L = [T] * (n + 1)
    for u in reversed(topo):
        for p in rev_adj[u]:
            if L[u] - 1 < L[p]:
                L[p] = L[u] - 1

    for u in range(1, n + 1):
        if E[u] > L[u] or E[u] > T or L[u] < 1:
            print("NO")
            return

    # Critical path length / depth for tie-breaking
    depth = [0] * (n + 1)
    for u in reversed(topo):
        d = 0
        for v in adj[u]:
            if depth[v] + 1 > d:
                d = depth[v] + 1
        depth[u] = d

    # Predecessor count needed dynamically
    pred_count = [len(rev_adj[i]) for i in range(n + 1)]
    slot_assigned = [0] * (n + 1)
    
    # Backtracking search slot by slot
    def search(slot, ready_tasks, assigned_count):
        if assigned_count == n:
            return True
        if slot > T:
            return False
        
        # Check deadline feasibility for all remaining tasks
        # If any ready or non-ready task has L[u] < slot, impossible
        # Also check interval capacity
        req_by_time = [0] * (T + 2)
        for u in range(1, n + 1):
            if slot_assigned[u] == 0:
                if L[u] < slot:
                    return False
                req_by_time[L[u]] += 1
        
        cum = 0
        for t in range(slot, T + 1):
            cum += req_by_time[t]
            if cum > (t - slot + 1) * M:
                return False
                
        # Tasks that MUST be done at `slot`
        mandatory = []
        optional = []
        for u in ready_tasks:
            if L[u] == slot:
                mandatory.append(u)
            else:
                optional.append(u)
                
        if len(mandatory) > M:
            return False
            
        cap_left = M - len(mandatory)
        
        # Sort optional tasks by urgency: L[u] asc, depth desc, len(adj[u]) desc
        optional.sort(key=lambda u: (L[u], -depth[u], -len(adj[u])))
        
        if len(optional) <= cap_left:
            candidates = [optional]
        else:
            # Generate combinations of size cap_left from top candidates
            # Heuristic: only consider a small pool of best optional tasks
            pool_size = min(len(optional), cap_left + 4)
            pool = optional[:pool_size]
            candidates = itertools.combinations(pool, cap_left)
            
        for opt_chosen in candidates:
            chosen = mandatory + list(opt_chosen)
            
            # Apply chosen
            newly_ready = []
            for u in chosen:
                slot_assigned[u] = slot
                for v in adj[u]:
                    pred_count[v] -= 1
                    if pred_count[v] == 0:
                        newly_ready.append(v)
            
            next_ready = [u for u in ready_tasks if slot_assigned[u] == 0] + newly_ready
            
            if search(slot + 1, next_ready, assigned_count + len(chosen)):
                return True
                
            # Rollback
            for u in chosen:
                slot_assigned[u] = 0
                for v in adj[u]:
                    pred_count[v] += 1

        return False

    initial_ready = [u for u in range(1, n + 1) if pred_count[u] == 0]
    
    if search(1, initial_ready, 0):
        print("YES")
        print(*(slot_assigned[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()