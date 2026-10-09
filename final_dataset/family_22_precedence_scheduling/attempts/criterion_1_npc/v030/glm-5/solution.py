import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr]); ptr += 1
    M = int(input[ptr]); ptr += 1
    T = int(input[ptr]); ptr += 1
    m = int(input[ptr]); ptr += 1

    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    
    for _ in range(m):
        a = int(input[ptr]); ptr += 1
        b = int(input[ptr]); ptr += 1
        adj[a].append(b)
        indeg[b] += 1
    
    # Earliest stage (1-indexed) for each dish
    min_t = [1] * (n + 1)
    q = deque()
    
    # Kahn's for topological sort and min stage
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)
    
    sorted_nodes = []
    while q:
        u = q.popleft()
        sorted_nodes.append(u)
        for v in adj[u]:
            if min_t[v] < min_t[u] + 1:
                min_t[v] = min_t[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(sorted_nodes) != n:
        print("NO")
        return
    
    # Check bounds
    for i in range(1, n + 1):
        if min_t[i] > T:
            print("NO")
            return
    
    # Compute latest stage (latest finish for topological order)
    max_t = [T] * (n + 1)
    # Process nodes in reverse topological order
    for u in reversed(sorted_nodes):
        for v in adj[u]:
            if max_t[u] > max_t[v] - 1:
                max_t[u] = max_t[v] - 1
    
    for i in range(1, n + 1):
        if min_t[i] > max_t[i]:
            print("NO")
            return
    
    # Check if total sum of lower bounds exceeds capacity
    cnt_min = [0] * (T + 2)
    for i in range(1, n + 1):
        cnt_min[min_t[i]] += 1
    
    q_min = deque()
    balance = [0] * (T + 2)
    needed = [0] * (T + 2)
    
    for t in range(1, T + 1):
        if t > 1:
            balance[t] = balance[t - 1]
        balance[t] += cnt_min[t]
        balance[t] -= M
        needed[t] = needed[t - 1] + max(0, -balance[t])
        if balance[t] > 0:
            # We have excess pressure, can push to the right if valid
            if t < T:
                balance[t + 1] = balance[t]  # Carry over positive balance
                balance[t] = 0
            else:
                # At last stage, still exceeding capacity
                print("NO")
                return
    
    # Form pairs and stages
    dishes = []
    for i in range(1, n + 1):
        dishes.append((min_t[i], max_t[i], i))
    dishes.sort()
    
    res = [0] * (n + 1)
    # Active sets: heaps containing -max_t for dishes available at stage t
    active_available = []
    # Already assigned with fixed stage (due to needed[t] requirements)
    # We manage balance and assignment.
    
    # current_balance[t] tracks dishes assigned at stage t
    # We construct assignment going stage by stage 1..T
    assigned_at_stage = [0] * (T + 1)
    
    dish_ptr = 0
    import heapq
    active = []  # min-heap of (max_t, index)
    
    for t in range(1, T + 1):
        # Add dishes whose min_t is <= t
        while dish_ptr < n and dishes[dish_ptr][0] <= t:
            heapq.heappush(active, (dishes[dish_ptr][1], dishes[dish_ptr][2]))
            dish_ptr += 1
        
        # First, satisfy needed[t] constraints by deferring dishes
        can_defer = needed[t] - (assigned_at_stage[t - 1] if t > 0 else 0)
        defer_pool = []
        # Pop dishes with max_t == t (must be assigned now)
        must_assign_now = []
        others = []
        
        temp = []
        while active:
            mt, idx = heapq.heappop(active)
            if mt == t:
                must_assign_now.append((mt, idx))
            else:
                temp.append((mt, idx))
        for item in temp:
            heapq.heappush(active, item)
        
        # Assign must_assign_now
        for mt, idx in must_assign_now:
            assigned_at_stage[t] += 1
            res[idx] = t
        # If after assigning must_assign_now we exceed capacity, fail
        if assigned_at_stage[t] > M:
            print("NO")
            return
        
        # Now fill remaining capacity greedily with earliest deadline
        while assigned_at_stage[t] < M and active:
            mt, idx = heapq.heappop(active)
            assigned_at_stage[t] += 1
            res[idx] = t
        
        # Check if any dish remained that must be assigned now but wasn't
        # (covered by checking active empty? No, must_assign_now handled)
        # Also check if any dish with min_t <= t remains in active for future
        # That's fine as long as min_t <= t <= max_t.
    
    # All dishes should be assigned
    if any(res[i] == 0 for i in range(1, n + 1)):
        print("NO")
        return
    
    # Final capacity check
    counts = [0] * (T + 1)
    for i in range(1, n + 1):
        counts[res[i]] += 1
    if any(counts[t] > M for t in range(1, T + 1)):
        print("NO")
        return
    
    print("YES")
    print(' '.join(str(res[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()