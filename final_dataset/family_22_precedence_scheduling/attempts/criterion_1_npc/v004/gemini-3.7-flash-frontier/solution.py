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
    in_deg = [0] * (n + 1)
    out_deg = [0] * (n + 1)
    
    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        rev_adj[v].append(u)
        in_deg[v] += 1
        out_deg[u] += 1

    # Check if total tasks exceed total capacity
    if n > M * T:
        print("NO")
        return

    # Topological sort to detect cycles and compute earliest / latest slots
    q = deque([i for i in range(1, n + 1) if in_deg[i] == 0])
    topo = []
    earliest = [1] * (n + 1)
    
    in_deg_copy = list(in_deg)
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            if earliest[u] + 1 > earliest[v]:
                earliest[v] = earliest[u] + 1
            in_deg_copy[v] -= 1
            if in_deg_copy[v] == 0:
                q.append(v)
                
    if len(topo) < n:
        # Cycle detected
        print("NO")
        return

    # Compute height / latest slot
    height = [1] * (n + 1)
    for u in reversed(topo):
        for v in adj[u]:
            if height[v] + 1 > height[u]:
                height[u] = height[v] + 1
                
    latest = [T - height[u] + 1 for u in range(n + 1)]
    
    for u in range(1, n + 1):
        if earliest[u] > latest[u] or latest[u] < 1 or earliest[u] > T:
            print("NO")
            return

    # Count total descendants for tie-breaking
    desc_count = [0] * (n + 1)
    for u in reversed(topo):
        # bitset / set of descendants
        # for performance, just sum of descendant heights or simple count
        desc_count[u] = 1 + sum(desc_count[v] for v in adj[u])

    # Greedy list scheduling
    def try_greedy(priority_key):
        cur_in_deg = list(in_deg)
        slot = [0] * (n + 1)
        available = [i for i in range(1, n + 1) if cur_in_deg[i] == 0]
        
        for t in range(1, T + 1):
            if not available:
                if all(slot[i] > 0 for i in range(1, n + 1)):
                    return slot
                continue
                
            available.sort(key=priority_key, reverse=True)
            
            # Select up to M tasks
            selected = available[:M]
            available = available[M:]
            
            next_avail = []
            for u in selected:
                slot[u] = t
                for v in adj[u]:
                    cur_in_deg[v] -= 1
                    if cur_in_deg[v] == 0:
                        next_avail.append(v)
            available.extend(next_avail)
            
        if all(slot[i] > 0 for i in range(1, n + 1)):
            return slot
        return None

    # Priority rules
    heuristics = [
        lambda x: (-latest[x], height[x], desc_count[x], out_deg[x]),
        lambda x: (height[x], -latest[x], desc_count[x]),
        lambda x: (desc_count[x], -latest[x], height[x]),
        lambda x: (-latest[x], out_deg[x]),
    ]
    
    for h in heuristics:
        res = try_greedy(h)
        if res is not None:
            print("YES")
            print(*(res[1:]))
            return

    # Backtracking search with strong pruning if heuristics alone don't solve it
    import itertools

    slot_assignment = [0] * (n + 1)
    cur_in_deg = list(in_deg)
    
    def backtrack(t, available):
        # If all tasks scheduled
        if not available and all(cur_in_deg[i] == 0 and slot_assignment[i] > 0 for i in range(1, n + 1)):
            return True
        if t > T:
            return False

        # Pruning 1: Any available or unscheduled task exceeding latest
        unscheduled = [i for i in range(1, n + 1) if slot_assignment[i] == 0]
        for u in unscheduled:
            if latest[u] < t:
                return False

        # Pruning 2: Capacity check for future intervals
        counts = [0] * (T + 2)
        for u in unscheduled:
            counts[latest[u]] += 1
        cum = 0
        for k in range(t, T + 1):
            cum += counts[k]
            if cum > (k - t + 1) * M:
                return False

        # Mandatory tasks that must be scheduled at time t
        mandatory = [u for u in available if latest[u] == t]
        if len(mandatory) > M:
            return False

        if len(available) <= M:
            chosen_combinations = [available]
        else:
            optional = [u for u in available if latest[u] > t]
            optional.sort(key=lambda x: (-latest[x], height[x], desc_count[x]), reverse=True)
            k = M - len(mandatory)
            # Take combinations of optional tasks, prioritized
            chosen_combinations = [mandatory + list(comb) for comb in itertools.islice(itertools.combinations(optional, k), 10)]

        for chosen in chosen_combinations:
            new_avail = [u for u in available if u not in chosen]
            next_avail = []
            for u in chosen:
                slot_assignment[u] = t
                for v in adj[u]:
                    cur_in_deg[v] -= 1
                    if cur_in_deg[v] == 0:
                        next_avail.append(v)

            if backtrack(t + 1, new_avail + next_avail):
                return True

            # Undo
            for u in chosen:
                slot_assignment[u] = 0
                for v in adj[u]:
                    cur_in_deg[v] += 1

        return False

    init_avail = [i for i in range(1, n + 1) if in_deg[i] == 0]
    if backtrack(1, init_avail):
        print("YES")
        print(*(slot_assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()