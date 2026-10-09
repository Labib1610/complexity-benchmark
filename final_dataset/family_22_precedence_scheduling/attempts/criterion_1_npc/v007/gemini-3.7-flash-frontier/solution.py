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
        out_degree[u] += 1
        in_degree[v] += 1

    # Check for cycles & compute earliest start time (1-indexed)
    earliest = [1] * (n + 1)
    q = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    visited_count = 0
    
    in_deg_copy = list(in_degree)
    while q:
        u = q.popleft()
        visited_count += 1
        for v in adj[u]:
            if earliest[u] + 1 > earliest[v]:
                earliest[v] = earliest[u] + 1
            in_deg_copy[v] -= 1
            if in_deg_copy[v] == 0:
                q.append(v)
                
    if visited_count < n:
        print("NO")
        return

    # Compute latest start time
    latest = [T] * (n + 1)
    out_deg_copy = list(out_degree)
    q = deque([i for i in range(1, n + 1) if out_degree[i] == 0])
    
    while q:
        u = q.popleft()
        for p in rev_adj[u]:
            if latest[u] - 1 < latest[p]:
                latest[p] = latest[u] - 1
            out_deg_copy[p] -= 1
            if out_deg_copy[p] == 0:
                q.append(p)

    for i in range(1, n + 1):
        if earliest[i] > latest[i] or latest[i] < 1 or earliest[i] > T:
            print("NO")
            return

    # Backtracking / Search
    # State: current slot t (from 1 to T), remaining in-degree for unscheduled tasks
    # We can schedule slot by slot.
    
    # Priority for choosing tasks: smaller latest[u], then larger remaining depth
    depth = [1] * (n + 1)
    # compute longest path to sink for tie breaking
    topo_order = []
    in_deg_copy = list(in_degree)
    q = deque([i for i in range(1, n + 1) if in_deg_copy[i] == 0])
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            in_deg_copy[v] -= 1
            if in_deg_copy[v] == 0:
                q.append(v)
                
    for u in reversed(topo_order):
        for v in adj[u]:
            if depth[v] + 1 > depth[u]:
                depth[u] = depth[v] + 1

    current_in_deg = list(in_degree)
    assigned_slot = [0] * (n + 1)
    
    # We can use a recursive search with memoization/pruning
    # To prune states, dynamically check feasibility:
    # 1. Any available task with latest == t MUST be scheduled at t.
    # 2. Total unscheduled tasks <= (T - t + 1) * M.
    
    def search(t, available):
        # available is a list of tasks ready to be scheduled
        num_unscheduled = sum(1 for i in range(1, n + 1) if assigned_slot[i] == 0)
        if num_unscheduled == 0:
            return True
        if t > T:
            return False
        if num_unscheduled > (T - t + 1) * M:
            return False

        # Tasks that MUST be scheduled at or before t
        # If any unscheduled task has latest[u] < t, impossible
        # If an available task has latest[u] == t, it must be scheduled now.
        must_schedule = []
        optional = []
        for u in available:
            if latest[u] < t:
                return False
            elif latest[u] == t:
                must_schedule.append(u)
            else:
                optional.append(u)

        # Check all unscheduled tasks for deadline violation
        for u in range(1, n + 1):
            if assigned_slot[u] == 0 and latest[u] < t:
                return False

        if len(must_schedule) > M:
            return False

        # Sort optional by (latest[u], -depth[u])
        optional.sort(key=lambda u: (latest[u], -depth[u]))

        needed = M - len(must_schedule)
        
        # We generate candidate subsets of tasks to schedule at slot t.
        # Candidate subsets always include all of `must_schedule`, plus up to `needed` from `optional`.
        # Usually taking greedily as many as possible (up to M) is optimal,
        # but we can branch on the number of optional tasks taken or combinations.
        
        # Heuristic: try largest subset first (greedy)
        from itertools import combinations
        
        # Limit branching to keep it fast
        # Try full capacity first, down to minimum needed
        max_opt = min(needed, len(optional))
        
        # If all optional tasks fit, just take all of them (up to M)
        # Otherwise, try combinations
        found = False
        for k in range(max_opt, -1, -1):
            if len(must_schedule) + k == 0 and num_unscheduled > 0 and t == T:
                continue
            
            # If k == max_opt and len(optional) <= 10:
            # try combinations of size k from optional
            # Prioritize prefix of sorted optional
            combos = []
            if k == len(optional):
                combos = [tuple(optional)]
            elif k == 0:
                combos = [()]
            else:
                # generate combinations, prioritizing earlier elements in optional
                # to prevent exponential blowup, take best prefix or standard combinations if small
                if len(optional) <= 15:
                    combos = list(combinations(optional, k))
                else:
                    # just take the best k, and a few variations
                    combos = [tuple(optional[:k])]
                    if k < len(optional):
                        combos.append(tuple(optional[:k-1] + [optional[k]]))
            
            for opt_choice in combos:
                chosen = must_schedule + list(opt_choice)
                
                # Apply choice
                for u in chosen:
                    assigned_slot[u] = t
                
                new_available = [u for u in available if u not in chosen]
                newly_freed = []
                for u in chosen:
                    for v in adj[u]:
                        current_in_deg[v] -= 1
                        if current_in_deg[v] == 0:
                            newly_freed.append(v)
                            new_available.append(v)
                            
                if search(t + 1, new_available):
                    return True
                
                # Revert
                for u in chosen:
                    assigned_slot[u] = 0
                for v in newly_freed:
                    current_in_deg[v] += 1
                for u in chosen:
                    for v in adj[u]:
                        if v not in newly_freed:
                            current_in_deg[v] += 1

            # If we filled the slot to capacity or took all available, usually sufficient
            if k == max_opt and len(must_schedule) + k == M:
                # If capacity is saturated, don't try smaller k unless backtracking forces it
                break

        return False

    initial_available = [i for i in range(1, n + 1) if in_degree[i] == 0]
    if search(1, initial_available):
        print("YES")
        print(*(assigned_slot[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()