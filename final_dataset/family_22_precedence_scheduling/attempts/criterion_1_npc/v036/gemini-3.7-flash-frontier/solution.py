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
    
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    in_deg_init = [0] * (n + 1)
    
    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        rev_adj[v].append(u)
        in_deg_init[v] += 1

    # Topological sort & Cycle check
    in_deg = list(in_deg_init)
    queue = [i for i in range(1, n + 1) if in_deg[i] == 0]
    topo_order = []
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        topo_order.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)
                
    if len(topo_order) < n:
        print("NO")
        return

    # Earliest stage (E) and Latest stage (L)
    E = [1] * (n + 1)
    for u in topo_order:
        for v in adj[u]:
            if E[u] + 1 > E[v]:
                E[v] = E[u] + 1

    L = [T] * (n + 1)
    for u in reversed(topo_order):
        for v in adj[u]:
            if L[v] - 1 < L[u]:
                L[u] = L[v] - 1

    for i in range(1, n + 1):
        if E[i] > L[i] or E[i] > T:
            print("NO")
            return

    # Height / Longest path to sink for tie-breaking
    height = [0] * (n + 1)
    for u in reversed(topo_order):
        h = 0
        for v in adj[u]:
            if height[v] + 1 > h:
                h = height[v] + 1
        height[u] = h

    # State tracking
    current_in_deg = list(in_deg_init)
    stage_assigned = [0] * (n + 1)
    assigned = [False] * (n + 1)

    import itertools

    steps_limit = [50000]

    def backtrack(stage, remaining_count):
        if remaining_count == 0:
            return True
        if stage > T:
            return False
        
        steps_limit[0] -= 1
        if steps_limit[0] <= 0:
            return False

        # Check deadline feasibility for all unassigned nodes
        must_pick = []
        ready_optional = []

        for i in range(1, n + 1):
            if not assigned[i]:
                if L[i] < stage:
                    return False
                if current_in_deg[i] == 0:
                    if L[i] == stage:
                        must_pick.append(i)
                    else:
                        ready_optional.append(i)

        if len(must_pick) > M:
            return False

        capacity_left = M - len(must_pick)
        # Sort optional by heuristic: smallest L, then largest height, then largest out-degree
        ready_optional.sort(key=lambda x: (L[x], -height[x], -len(adj[x])))

        # Generate candidate subsets of optional to pick
        # Greedily prefer taking as many as possible
        candidates = []
        max_take = min(capacity_left, len(ready_optional))
        
        # Priority 1: take top max_take elements
        best_opt = tuple(ready_optional[:max_take])
        candidates.append(best_opt)

        # If we need to branch, try other combinations
        if max_take > 0 and len(ready_optional) > max_take:
            # Add a few alternative combinations from top candidates
            pool = ready_optional[:min(len(ready_optional), max_take + 3)]
            for comb in itertools.combinations(pool, max_take):
                if comb != best_opt:
                    candidates.append(comb)
                    if len(candidates) >= 5:
                        break

        # Also try taking fewer if possible, though rarely optimal
        # Usually list scheduling with full capacity is best.

        for opt_comb in candidates:
            chosen = must_pick + list(opt_comb)
            
            # Apply choice
            for u in chosen:
                assigned[u] = True
                stage_assigned[u] = stage
                for v in adj[u]:
                    current_in_deg[v] -= 1
            
            if backtrack(stage + 1, remaining_count - len(chosen)):
                return True

            # Undo choice
            for u in chosen:
                assigned[u] = False
                stage_assigned[u] = 0
                for v in adj[u]:
                    current_in_deg[v] += 1

        return False

    if backtrack(1, n):
        print("YES")
        print(*(stage_assigned[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()