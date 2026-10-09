import sys

# Increase recursion depth for deep dependency chains
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
    in_degree = [0] * (n + 1)
    
    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        rev_adj[v].append(u)
        in_degree[v] += 1

    # Cycle detection and topological sort
    deg = list(in_degree)
    queue = [i for i in range(1, n + 1) if deg[i] == 0]
    topo_order = []
    
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        topo_order.append(u)
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                queue.append(v)
                
    if len(topo_order) < n:
        print("NO")
        return

    # Compute Earliest Start Time (L)
    L = [1] * (n + 1)
    for u in topo_order:
        for v in adj[u]:
            if L[u] + 1 > L[v]:
                L[v] = L[u] + 1

    # Compute Latest Start Time (R)
    R = [T] * (n + 1)
    for u in reversed(topo_order):
        for p in rev_adj[u]:
            if R[u] - 1 < R[p]:
                R[p] = R[u] - 1

    for i in range(1, n + 1):
        if L[i] > R[i] or L[i] > T or R[i] < 1:
            print("NO")
            return

    # Backtracking / List Scheduling
    # Priority for list scheduling:
    # 1. R[v] (Earliest Deadline First)
    # 2. Number of descendants / path length
    
    height = [0] * (n + 1)
    for u in reversed(topo_order):
        h = 0
        for v in adj[u]:
            if height[v] + 1 > h:
                h = height[v] + 1
        height[u] = h

    assigned_phase = [0] * (n + 1)
    current_in_degree = list(in_degree)
    
    # Ready items initially
    ready = [i for i in range(1, n + 1) if current_in_degree[i] == 0]

    def search(phase, ready_set):
        if phase > T:
            return all(assigned_phase[i] > 0 for i in range(1, n + 1))
        
        # Check mandatory items that MUST be scheduled at or before this phase
        mandatory = []
        optional = []
        for u in ready_set:
            if R[u] == phase:
                mandatory.append(u)
            elif R[u] > phase:
                optional.append(u)
            else:
                # R[u] < phase means it's already expired!
                return False
                
        if len(mandatory) > M:
            return False
            
        # Sort optional by (R[u], -height[u])
        optional.sort(key=lambda u: (R[u], -height[u]))
        
        # We can pick mandatory + up to (M - len(mandatory)) from optional
        needed = M - len(mandatory)
        to_schedule = mandatory + optional[:needed]
        
        # Apply choices
        new_ready = list(optional[needed:])
        for u in to_schedule:
            assigned_phase[u] = phase
            for v in adj[u]:
                current_in_degree[v] -= 1
                if current_in_degree[v] == 0:
                    new_ready.append(v)
                    
        if search(phase + 1, new_ready):
            return True
            
        # Backtrack
        for u in to_schedule:
            assigned_phase[u] = 0
            for v in adj[u]:
                current_in_degree[v] += 1
                
        return False

    if search(1, ready):
        print("YES")
        print(*(assigned_phase[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()