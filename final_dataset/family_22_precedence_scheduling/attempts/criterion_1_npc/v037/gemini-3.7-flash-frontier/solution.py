import sys
from collections import deque

# Increase recursion depth just in case
sys.setrecursionlimit(20000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        M = int(next(iterator))
        D = int(next(iterator))
        K = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(N + 1)]
    radj = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    
    for _ in range(K):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        radj[v].append(u)
        in_degree[v] += 1

    # Cycle detection and topological sort
    q = deque([i for i in range(1, N + 1) if in_degree[i] == 0])
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if len(topo_order) < N:
        print("NO")
        return

    # Earliest start slot (1-indexed)
    es = [1] * (N + 1)
    for u in topo_order:
        for v in adj[u]:
            if es[u] + 1 > es[v]:
                es[v] = es[u] + 1

    # Latest start slot (1-indexed)
    ls = [D] * (N + 1)
    for u in reversed(topo_order):
        for v in adj[u]:
            if ls[v] - 1 < ls[u]:
                ls[u] = ls[v] - 1

    for i in range(1, N + 1):
        if es[i] > ls[i] or es[i] > D or ls[i] < 1:
            print("NO")
            return

    # Transitive closure / successors depth for heuristic
    depth = [0] * (N + 1)
    for u in reversed(topo_order):
        d = 0
        for v in adj[u]:
            if depth[v] + 1 > d:
                d = depth[v] + 1
        depth[u] = d

    assigned_slot = [0] * (N + 1)
    pred_count = [len(radj[i]) for i in range(N + 1)]
    
    # State representation for memoization:
    # (slot, unscheduled_mask or tuple of unscheduled)
    # But N might be up to 100+, bitmask might be large or memoization on state of unscheduled tasks.
    # We can use a randomized/heuristic backtracking or DFS with priority.

    def backtrack(slot, ready_tasks, remaining_preds):
        if slot > D:
            # Check if all tasks are scheduled
            for i in range(1, N + 1):
                if assigned_slot[i] == 0:
                    return False
            return True

        # Check critical tasks that MUST be scheduled at or before 'slot'
        # Any unscheduled task with ls[task] == slot must be scheduled now.
        must_schedule = []
        can_schedule = []
        for u in ready_tasks:
            if ls[u] < slot:
                return False
            elif ls[u] == slot:
                must_schedule.append(u)
            else:
                can_schedule.append(u)

        # Check if there are any unscheduled non-ready tasks with ls <= slot
        # (This is already impossible since their unscheduled preds would have even smaller ls,
        # but let's be safe: if a task has ls <= slot and is not ready, some pred has ls < slot <= slot,
        # which would have failed earlier or will be detected).
        
        if len(must_schedule) > M:
            return False

        # If must_schedule + can_schedule is small, we choose combinations
        slots_left = M - len(must_schedule)
        
        # Sort can_schedule by priority:
        # 1. smallest ls
        # 2. largest depth (longest path to sink)
        # 3. largest number of successors
        can_schedule.sort(key=lambda x: (ls[x], -depth[x], -len(adj[x])))

        # Generate candidate subsets of can_schedule of size <= slots_left
        # To avoid combinatorial explosion, if there are many candidates,
        # prioritize taking up to slots_left from the best candidates.
        # Generating subsets in order of preference:
        import itertools
        
        # Choose how many to pick: from min(slots_left, len(can_schedule)) down to 0
        # Usually it's strictly better to schedule more tasks, except in rare anomaly cases.
        # But generally greedy on size is optimal or near-optimal.
        max_take = min(slots_left, len(can_schedule))

        # We try larger subsets first
        def get_subsets():
            for k in range(max_take, -1, -1):
                # To limit branch factor, if can_schedule is large, consider top candidates
                pool = can_schedule[:min(len(can_schedule), k + 4)]
                for comb in itertools.combinations(pool, k):
                    yield list(comb)

        for comb in get_subsets():
            chosen = must_schedule + comb
            
            # Apply chosen
            new_ready = [x for x in ready_tasks if x not in chosen]
            for u in chosen:
                assigned_slot[u] = slot
                for v in adj[u]:
                    remaining_preds[v] -= 1
                    if remaining_preds[v] == 0:
                        new_ready.append(v)

            if backtrack(slot + 1, new_ready, remaining_preds):
                return True

            # Undo chosen
            for u in chosen:
                assigned_slot[u] = 0
                for v in adj[u]:
                    remaining_preds[v] += 1

        return False

    init_ready = [i for i in range(1, N + 1) if pred_count[i] == 0]
    
    if backtrack(1, init_ready, pred_count):
        print("YES")
        print(*(assigned_slot[i] for i in range(1, N + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()