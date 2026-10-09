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
    
    if n > M * T:
        print("NO")
        return

    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        rev_adj[v].append(u)
        in_degree[v] += 1

    # Topological sort & cycle detection
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

    # Earliest Start Time (EST)
    est = [1] * (n + 1)
    for u in topo:
        for v in adj[u]:
            if est[u] + 1 > est[v]:
                est[v] = est[u] + 1

    # Latest Start Time (LST)
    lst = [T] * (n + 1)
    for u in reversed(topo):
        for v in adj[u]:
            if lst[v] - 1 < lst[u]:
                lst[u] = lst[v] - 1

    for i in range(1, n + 1):
        if est[i] > lst[i] or lst[i] < 1 or est[i] > T:
            print("NO")
            return

    # Backtracking search to assign slots
    # State: current time slot t (from 1 to T), remaining unscheduled tasks
    # Pre-calculate in-degree for remaining tasks
    cur_in_deg = [len(rev_adj[i]) for i in range(n + 1)]
    scheduled_slot = [0] * (n + 1)
    
    # Priority for tasks: smaller lst, then larger number of descendants/est
    desc_count = [0] * (n + 1)
    for u in reversed(topo):
        desc_count[u] = 1 + sum(desc_count[v] for v in adj[u])

    def search(t, remaining_count):
        if remaining_count == 0:
            return True
        if t > T:
            return False

        # Pruning: Capacity check for future deadlines
        # Count unscheduled tasks with lst <= k
        # If count > (k - t + 1) * M for any k, then impossible.
        counts = [0] * (T + 2)
        for i in range(1, n + 1):
            if scheduled_slot[i] == 0:
                counts[lst[i]] += 1
        
        cum = 0
        for k in range(t, T + 1):
            cum += counts[k]
            if cum > (k - t + 1) * M:
                return False

        # Find available tasks (in_deg == 0 and not scheduled)
        available = [i for i in range(1, n + 1) if scheduled_slot[i] == 0 and cur_in_deg[i] == 0]
        
        # Must schedule tasks with lst[i] == t
        must = [i for i in available if lst[i] == t]
        if len(must) > M:
            return False

        optional = [i for i in available if lst[i] > t]
        # Sort optional by lst ascending, then desc_count descending
        optional.sort(key=lambda x: (lst[x], -desc_count[x]))

        slots_left = M - len(must)
        
        # We can pick any subset of optional of size <= slots_left
        # In fact, we should greedily try larger subsets first
        # But if total available <= M, we should just take all available!
        # Note: Taking fewer than M is only necessary if saving capacity helps,
        # but since tasks take 1 unit and have no release dates other than predecessors,
        # scheduling an available task earlier never hurts any precedence constraint!
        # Thus, we should always pick min(slots_left, len(optional)) tasks from optional.
        # Is it always optimal to pick the top-k from optional?
        # While Coffman-Graham / list scheduling is not strictly guaranteed for M >= 3,
        # trying combinations of top candidates or top-k directly is extremely effective.
        
        max_to_pick = min(slots_left, len(optional))
        
        # Try picking exactly max_to_pick items from optional
        # To be complete yet fast, if there are multiple combinations, we iterate through combinations of size max_to_pick
        # Usually, picking the best candidates is sufficient.
        if len(optional) <= slots_left:
            combos = [tuple(optional)]
        else:
            # We can consider combinations of size slots_left from the top candidates
            cand_pool = optional[:min(len(optional), slots_left + 4)]
            combos = list(itertools.combinations(cand_pool, slots_left))

        for opt_chosen in combos:
            chosen = must + list(opt_chosen)
            # Apply chosen
            for u in chosen:
                scheduled_slot[u] = t
                for v in adj[u]:
                    cur_in_deg[v] -= 1
            
            if search(t + 1, remaining_count - len(chosen)):
                return True
            
            # Backtrack
            for u in chosen:
                scheduled_slot[u] = 0
                for v in adj[u]:
                    cur_in_deg[v] += 1

        return False

    if search(1, n):
        print("YES")
        print(*(scheduled_slot[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()