import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n)]
    in_deg = [0] * n
    
    # Kahn's algorithm related structures
    q = deque()
    
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        in_deg[v] += 1

    # Compute earliest possible phase for each node (longest path length from sources)
    earliest = [1] * n
    # We perform a standard topological sort to process nodes in an order that allows optimal propagation of earliest times
    # We maintain a separate queue for this logic, not the binary search queue
    q_topo = deque()
    copy_deg = in_deg[:]
    
    for i in range(n):
        if in_deg[i] == 0:
            q_topo.append(i)
            
    topo_order = []
    while q_topo:
        u = q_topo.popleft()
        topo_order.append(u)
        for v in adj[u]:
            earliest[v] = max(earliest[v], earliest[u] + 1)
            copy_deg[v] -= 1
            if copy_deg[v] == 0:
                q_topo.append(v)

    # If graph has cycle
    if len(topo_order) != n:
        print("NO")
        return

    # Feasibility check with allocation simulation
    # Buckets: counts[i] is the number of nodes assigned to phase i (1-based)
    # We only need counts, node identities don't matter for simulation
    # allowed_slots[i] = M if n <= M*T else computed based on earliest/latest
    
    # Compute latest possible phases
    # If n > M*T, impossible since each phase holds max M
    if n > M * T:
        print("NO")
        return

    # Compute latest deadlines
    # latest[u] = max time such that node u fits, considering its descendants
    latest = [T] * n
    for u in reversed(topo_order):
        for v in adj[u]:
            # u must be strictly before v, so u <= v - 1
            latest[u] = min(latest[u], latest[v] - 1)

    # Check if earliest <= latest for all
    for i in range(n):
        if earliest[i] > latest[i]:
            print("NO")
            return

    # Binary search for the particular allocatable earliest phases
    # Common pattern: one test sol checks for times <= T, another finds shift.
    # We perform one feasibility test for earliest times. If it passes, we have a valid vector.
    # If it fails, earliest++ might theoretically fix it, but we used binary search over delay.
    # Let's do binary search on the shift to find the minimum shift that makes it feasible.
    
    def check(shift):
        # Shifted earliest times
        times = [min(e + shift, T) for e in earliest]
        # Check integrity with latest
        for i in range(n):
            if times[i] > latest[i]:
                return False
        
        counts = [0] * (T + 2)
        for t in times:
            counts[t] += 1
        
        # Simulation
        for p in range(T, 0, -1):
            if counts[p] > M:
                overflow = counts[p] - M
                if p == 1: return False
                counts[p-1] += overflow
        
        # Check if phase 1 is valid
        return counts[1] <= M

    lo, hi = 0, T
    found_shift = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid):
            found_shift = mid
            hi = mid - 1
        else:
            lo = mid + 1
            
    if found_shift == -1:
        print("NO")
        return

    # Construct the assignment using found_shift
    res = [min(e + found_shift, T) for e in earliest]
    
    # Greedy correction: if a phase is overloaded, push excess to earlier phases
    # This greedy works backwards from T to 1.
    # Since we don't care which module moves, we can simply push counts.
    # But we need to assign specific modules.
    # Strategy: Sort modules by phase (descending), and reassign greedily.
    
    counts = [0] * (T + 2)
    for t in res: counts[t] += 1
    
    excess = [0] * (T + 2)
    for p in range(T + 1):
        if counts[p] > M:
            excess[p] = counts[p] - M
            
    # Reversed iteration for greedy assignment
    # We sort nodes by phase descending. We assign them to phases filling from T down to 1
    # maintaining counts. If a phase is full, we place in previous.
    
    nodes_by_phase = [[] for _ in range(T + 1)]
    for i in range(n):
        nodes_by_phase[res[i]].append(i)
        
    final_assignments = [-1] * n
    current_capacity = [M] * (T + 1)
    
    for p in range(T, 0, -1):
        # Process nodes nominally in phase p
        # They can be assigned to p, or if p is full, p-1, etc.
        # Queue of nodes to place, starting with those for p
        pool = list(nodes_by_phase[p])
        ptr = p
        while pool:
            # Find latest available phase <= ptr
            while ptr > 0 and current_capacity[ptr] == 0:
                ptr -= 1
            if ptr == 0:
                # Should not happen if feasibility guaranteed
                print("NO")
                return
            # Place one node
            u = pool.pop()
            final_assignments[u] = ptr
            current_capacity[ptr] -= 1
    
    # Validate
    valid = True
    for i in range(n):
        if final_assignments[i] == -1 or not (1 <= final_assignments[i] <= T):
            valid = False
            break
        if final_assignments[i] > latest[i] or final_assignments[i] < earliest[i]:
            valid = False
            break
    if valid:
        for u in range(n):
            for v in adj[u]:
                if final_assignments[u] >= final_assignments[v]:
                    valid = False
                    break
            if not valid: break
    
    if not valid:
        print("NO")
    else:
        print("YES")
        print(*(final_assignments))

if __name__ == "__main__":
    solve()