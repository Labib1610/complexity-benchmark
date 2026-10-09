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
        
    # Check for cycles & compute ASAP (E)
    E = [1] * (n + 1)
    q = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    topo_order = []
    
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
        
    # Compute ALAP (L)
    L = [T] * (n + 1)
    for u in reversed(topo_order):
        for v in adj[u]:
            if L[v] - 1 < L[u]:
                L[u] = L[v] - 1
                
    for i in range(1, n + 1):
        if E[i] > L[i] or E[i] > T or L[i] < 1:
            print("NO")
            return

    # Count descendants
    desc_count = [0] * (n + 1)
    for u in reversed(topo_order):
        desc = {u}
        for v in adj[u]:
            desc.add(v)
        desc_count[u] = len(desc)

    # Coffman-Graham labeling
    cg_label = [0] * (n + 1)
    out_deg_cg = list(out_degree)
    ready_cg = [i for i in range(1, n + 1) if out_deg_cg[i] == 0]
    
    for label in range(1, n + 1):
        if not ready_cg:
            break
        # Pick task whose sorted list of successor labels is lexicographically smallest
        best_cand = None
        best_succ_labels = None
        for u in ready_cg:
            succ_labels = sorted([cg_label[v] for v in adj[u]], reverse=True)
            if best_cand is None or succ_labels < best_succ_labels:
                best_cand = u
                best_succ_labels = succ_labels
        
        cg_label[best_cand] = label
        ready_cg.remove(best_cand)
        for p in rev_adj[best_cand]:
            out_deg_cg[p] -= 1
            if out_deg_cg[p] == 0:
                ready_cg.append(p)

    # Heuristic list scheduling attempts
    def try_greedy(key_func):
        cur_in_degree = list(in_degree)
        ready = [i for i in range(1, n + 1) if cur_in_degree[i] == 0]
        schedule = [0] * (n + 1)
        
        for t in range(1, T + 1):
            if not ready:
                break
            ready.sort(key=key_func)
            picked = ready[:M]
            ready = ready[M:]
            
            for u in picked:
                schedule[u] = t
                
            for u in picked:
                for v in adj[u]:
                    cur_in_degree[v] -= 1
                    if cur_in_degree[v] == 0:
                        ready.append(v)
                        
        if all(schedule[i] > 0 for i in range(1, n + 1)):
            return schedule
        return None

    # Try various heuristics
    heuristics = [
        lambda x: (L[x], -E[x], -desc_count[x]),
        lambda x: (-cg_label[x]),
        lambda x: (L[x], -cg_label[x]),
        lambda x: (-desc_count[x], L[x]),
        lambda x: (L[x], -len(adj[x]))
    ]
    
    for h in heuristics:
        res = try_greedy(h)
        if res is not None:
            print("YES")
            print(*(res[1:]))
            return

    # Backtracking search with branch and bound
    assigned_slot = [0] * (n + 1)
    visited = set()
    
    def get_combinations(cands, k):
        from itertools import combinations
        return combinations(cands, k)

    import itertools
    
    cur_in_degree = list(in_degree)
    
    def dfs(t, scheduled_mask):
        if scheduled_mask == (1 << n) - 1:
            return True
        if t > T:
            return False
            
        state_key = (t, scheduled_mask)
        if state_key in visited:
            return False
        if len(visited) > 200000:
            return False
        visited.add(state_key)
        
        # Identify ready tasks
        ready = []
        for i in range(1, n + 1):
            if not (scheduled_mask & (1 << (i - 1))) and cur_in_degree[i] == 0:
                ready.append(i)
                
        must = [i for i in ready if L[i] == t]
        if len(must) > M:
            return False
            
        other = [i for i in ready if L[i] > t]
        other.sort(key=lambda x: (L[x], -cg_label[x]))
        
        slots_left = M - len(must)
        if len(other) <= slots_left:
            choices = [must + other]
        else:
            choices = []
            for comb in itertools.combinations(other, slots_left):
                choices.append(must + list(comb))
                if len(choices) >= 20: # limit branching
                    break
                    
        for choice in choices:
            new_mask = scheduled_mask
            for u in choice:
                assigned_slot[u] = t
                new_mask |= (1 << (u - 1))
                for v in adj[u]:
                    cur_in_degree[v] -= 1
                    
            if dfs(t + 1, new_mask):
                return True
                
            for u in choice:
                assigned_slot[u] = 0
                for v in adj[u]:
                    cur_in_degree[v] += 1
                    
        return False

    if dfs(1, 0):
        print("YES")
        print(*(assigned_slot[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()