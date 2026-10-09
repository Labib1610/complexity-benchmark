import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    iterator = iter(input)
    
    try:
        n = int(next(iterator))
    except StopIteration:
        return
    
    M = int(next(iterator))
    T = int(next(iterator))
    m_count = int(next(iterator))
    
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    # Build a copy of edges to compute in-degrees later for topological sort
    edges = []

    for _ in range(m_count):
        u = int(next(iterator))
        v = int(next(iterator))
        edges.append((u, v))
    
    # Cycle 1: Build graph and check for cycles (Is it a DAG?)
    tmp_adj = [[] for _ in range(n + 1)]
    tmp_in_deg = [0] * (n + 1)
    
    for u, v in edges:
        tmp_adj[u].append(v)
        tmp_in_deg[v] += 1
        
    q = deque()
    for i in range(1, n + 1):
        if tmp_in_deg[i] == 0:
            q.append(i)
            
    vis_count = 0
    topo_order = []
    
    while q:
        u = q.popleft()
        topo_order.append(u)
        vis_count += 1
        for v in tmp_adj[u]:
            tmp_in_deg[v] -= 1
            if tmp_in_deg[v] == 0:
                q.append(v)
                
    if vis_count != n:
        print("NO")
        return

    # Cycle 2: Binary search for the minimum T_min span
    # Lower bound L: ceil(n / M), must be at least length of longest path
    # Upper bound R: T (given constraint)
    
    # Precompute longest path length for each node (number of nodes on the path)
    # Process in topological order
    dp_len = [1] * (n + 1)
    for u in topo_order:
        for v in tmp_adj[u]:
            if dp_len[v] < dp_len[u] + 1:
                dp_len[v] = dp_len[u] + 1
    
    max_path_len = 0
    for i in range(1, n + 1):
        if dp_len[i] > max_path_len:
            max_path_len = dp_len[i]
            
    L = max((n + M - 1) // M, max_path_len)
    R = T
    
    # If the span needed for dependencies exceeds available time, impossible
    if L > R:
        print("NO")
        return
        
    # Binary search
    ans_T = -1
    
    # We need to store the earliest possible cycles to verify feasibility
    res_assignment = [0] * (n + 1)
    
    low = L
    high = R
    
    while low <= high:
        mid = (low + high) // 2
        
        # Feasibility check: Can we schedule in 'mid' cycles?
        # Compute earliest possible cycle for each node
        earliest = [1] * (n + 1)
        possible = True
        
        for u in topo_order:
            for v in tmp_adj[u]:
                if earliest[v] < earliest[u] + 1:
                    earliest[v] = earliest[u] + 1
        
        # Check if any node exceeds the time limit 'mid'
        for i in range(1, n + 1):
            if earliest[i] > mid:
                possible = False
                break
        
        if not possible:
            low = mid + 1
            continue
        
        # Calculate prefix sums of capacity
        capacity_prefix = [0] * (mid + 2)
        for i in range(1, mid + 1):
            capacity_prefix[i] = capacity_prefix[i-1] + M
        
        # Store cnt array
        cnt = [0] * (mid + 2)
        
        # Process nodes in reverse topological order to assign latest possible cycles
        # We can use a list of indices sorted by earliest[u], then break ties by topological order?
        # The standard algorithm processes in topological sort order.
        # To ensure correctness with latest finish propagation, we process in reverse topological order.
        
        sorted_nodes = sorted(range(1, n + 1), key=lambda x: (earliest[x], topo_order.index(x)))
        
        for u in sorted_nodes:
            # Assign the latest possible cycle for u
            t = earliest[u]
            # Adjust t upwards if slots are full
            while cnt[t] == M:
                t += 1
            
            if t > mid:
                possible = False
                break
            
            cnt[t] += 1
        
        if possible:
            ans_T = mid
            # Check if we need to store assignment
            # We need to construct the final assignment for the found T
            high = mid - 1
        else:
            low = mid + 1
            
    if ans_T == -1:
        print("NO")
        return
        
    # Reconstruct the assignment for ans_T
    # This time we record the assignment
    
    # Recalculate earliest for the found ans_T
    earliest = [1] * (n + 1)
    for u in topo_order:
        for v in tmp_adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
                
    cnt = [0] * (ans_T + 2)
    assignment = [0] * (n + 1)
    
    sorted_nodes = sorted(range(1, n + 1), key=lambda x: (earliest[x], topo_order.index(x)))
    
    for u in sorted_nodes:
        t = earliest[u]
        while cnt[t] == M:
            t += 1
        assignment[u] = t
        cnt[t] += 1
        
    print("YES")
    print(*(assignment[1:]))

if __name__ == '__main__':
    solve()