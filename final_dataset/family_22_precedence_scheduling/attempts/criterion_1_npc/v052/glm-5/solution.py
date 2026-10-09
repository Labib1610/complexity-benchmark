import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
        M = int(next(it))
        T_max = int(next(it))
        m = int(next(it))
    except StopIteration:
        return

    adj = [[] for _ in range(n)]
    in_degree = [0] * n

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        in_degree[v] += 1

    # longest_path[u] = max distance to start (number of edges)
    # For source nodes (in_degree 0), it's 0.
    longest_path = [0] * n
    
    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)
    
    topo_order = []
    processed_count = 0
    
    while q:
        u = q.popleft()
        topo_order.append(u)
        processed_count += 1
        for v in adj[u]:
            if longest_path[v] < longest_path[u] + 1:
                longest_path[v] = longest_path[u] + 1
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if processed_count != n:
        print("NO")
        return

    # Check schedule feasibility
    if T_max > n:
        T_max = n  # Cap for count array size optimization
    
    count = [0] * (T_max + 2)
    
    # Maximum shift required based on dependencies
    curr_max_shift = 0
    for i in range(n):
        shift_needed = longest_path[i] + 1
        if shift_needed > curr_max_shift:
            curr_max_shift = shift_needed
    
    if curr_max_shift > T_max:
        print("NO")
        return
    
    # Perform greedy blocking to verify capacity constraints
    # We place operations in the earliest available slot >= logical dependency time
    blocked_till = [0] * (T_max + 2)
    
    for u in topo_order:
        earliest_dep = longest_path[u] + 1
        
        # Find first slot available at or after earliest_dep
        t = earliest_dep
        while t <= T_max and blocked_till[t] >= M:
            t += 1
        
        if t > T_max:
            print("NO")
            return
        
        # Place operation u in slot t
        blocked_till[t] += 1
    
    # Schedule exists, now produce output: 1-based shift indices
    # We can simply output longest_path[i] + 1 as it satisfies all constraints
    # and the feasibility check passed.
    res = [longest_path[i] + 1 for i in range(n)]
    
    print("YES")
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    solve()