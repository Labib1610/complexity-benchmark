import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

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
    in_deg = [0] * (n + 1)
    
    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        rev_adj[v].append(u)
        in_deg[v] += 1

    # Check for cycles and compute topological order
    from collections import deque
    q = deque([i for i in range(1, n + 1) if in_deg[i] == 0])
    topo_order = []
    
    temp_deg = list(in_deg)
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            temp_deg[v] -= 1
            if temp_deg[v] == 0:
                q.append(v)
                
    if len(topo_order) < n:
        print("NO")
        return

    # Compute E_u (Earliest Slot)
    E = [1] * (n + 1)
    for u in topo_order:
        for v in adj[u]:
            if E[u] + 1 > E[v]:
                E[v] = E[u] + 1
                
    # Compute L_u (Latest Slot) and Height
    L = [T] * (n + 1)
    height = [0] * (n + 1)
    for u in reversed(topo_order):
        for v in adj[u]:
            if L[v] - 1 < L[u]:
                L[u] = L[v] - 1
            if height[v] + 1 > height[u]:
                height[u] = height[v] + 1
                
    for i in range(1, n + 1):
        if E[i] > L[i] or L[i] < 1 or E[i] > T:
            print("NO")
            return

    # Priority key for candidate jobs: smaller L, larger height, larger out-degree
    out_deg = [len(adj[i]) for i in range(n + 1)]
    
    assigned_slot = [0] * (n + 1)
    cur_in_deg = list(in_deg)
    
    # Ready set
    ready = {i for i in range(1, n + 1) if cur_in_deg[i] == 0}
    
    # Backtracking search slot-by-slot
    def search(t, ready_set):
        if t > T:
            return all(assigned_slot[i] != 0 for i in range(1, n + 1))
        
        # Check unassigned jobs whose deadline is past or current
        # If any unassigned job has L[u] < t, impossible
        # If L[u] == t, it MUST be scheduled at slot t
        mand = []
        for u in range(1, n + 1):
            if assigned_slot[u] == 0:
                if L[u] < t:
                    return False
                if L[u] == t:
                    if u not in ready_set:
                        return False
                    mand.append(u)
                    
        if len(mand) > M:
            return False
        
        mand_set = set(mand)
        cands = [u for u in ready_set if u not in mand_set]
        # Sort candidates by heuristic: L ascending, height descending, out_deg descending
        cands.sort(key=lambda u: (L[u], -height[u], -out_deg[u]))
        
        rem_cap = M - len(mand)
        
        # We try combinations of candidates.
        # Most promising: take the top min(rem_cap, len(cands)) candidates.
        # We also generate fewer candidates if branching is needed.
        from itertools import combinations
        
        # To avoid massive branching, prioritize taking the largest prefix
        # and if necessary, other subsets of the top candidates
        max_take = min(rem_cap, len(cands))
        
        # First try taking as many best candidates as possible
        candidate_subsets = []
        if max_take == 0:
            candidate_subsets = [()]
        else:
            # We first try top max_take
            candidate_subsets.append(tuple(cands[:max_take]))
            # Then if pool is small, maybe other combinations
            pool_size = min(len(cands), max_take + 2)
            for k in range(max_take, -1, -1):
                for comb in combinations(cands[:pool_size], k):
                    if comb != tuple(cands[:max_take]):
                        candidate_subsets.append(comb)
                        if len(candidate_subsets) > 15: # limit branching factor
                            break
                if len(candidate_subsets) > 15:
                    break

        for chosen_cands in candidate_subsets:
            chosen = mand + list(chosen_cands)
            
            # Apply chosen
            new_ready = set(ready_set)
            for u in chosen:
                assigned_slot[u] = t
                new_ready.remove(u)
                
            for u in chosen:
                for v in adj[u]:
                    cur_in_deg[v] -= 1
                    if cur_in_deg[v] == 0:
                        new_ready.add(v)
                        
            if search(t + 1, new_ready):
                return True
                
            # Revert
            for u in chosen:
                for v in adj[u]:
                    cur_in_deg[v] += 1
                assigned_slot[u] = 0

        return False

    if search(1, ready):
        print("YES")
        print(*(assigned_slot[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()