import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    pairs = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        pairs.append((u, v))
    
    # Greedy strategy: place module 1 at position 1, then 2, 3, ..., n.
    # This minimizes separation for edges (i, i+1).
    
    # Max possible total length: sum of (n-1) + (n-2) + ... + 1 = n*(n-1)//2
    # Edges like (1, n) would incur max cost n-1 in this placement.
    
    # Check if the budget is feasible for any placement.
    # Worst case budget needed corresponds to sum of max separations.
    # Max separation = n-1.
    # If B >= m * (n - 1), it is definitely possible.
    
    max_total_possible = m * (n - 1)
    if B > max_total_possible:
        # Result is trivially YES.
        # Output the standard placement.
        print("YES")
        print(*(range(1, n + 1)))
        return
    
    # If B is small, we apply a heuristic optimization.
    # We use a modified degree-based greedy for relative ordering, 
    # then reverse if it exceeds budget.
    # This handles cases like edges (1, n) which need reversed placement.
    
    deg = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for u, v in pairs:
        deg[u] += 1
        deg[v] += 1
        adj[u].append(v)
        adj[v].append(u)
    
    order = list(range(1, n + 1))
    # Sort by degree descending
    order.sort(key=lambda x: -deg[x])
    
    placement = [0] * (n + 1)
    for i, module_id in enumerate(order):
        placement[module_id] = i + 1
        
    # Calculate total length
    total = 0
    for u, v in pairs:
        total += abs(placement[u] - placement[v])
    
    if total <= B:
        print("YES")
        print(*(placement[1:]))
        return
    
    # Try reversed placement: high degree at ends?
    # Reverse the sorted order: high degree at n, low at 1.
    placement_rev = [0] * (n + 1)
    for i, module_id in enumerate(order):
        placement_rev[module_id] = n - i
        
    total_rev = 0
    for u, v in pairs:
        total_rev += abs(placement_rev[u] - placement_rev[v])
    
    if total_rev <= B:
        print("YES")
        print(*(placement_rev[1:]))
        return
    
    # If still not found, check standard linear placement.
    # It addresses cases with chains like (1,2), (2,3) which favor proximity.
    placement_lin = list(range(n + 1))
    total_lin = 0
    for u, v in pairs:
        total_lin += abs(placement_lin[u] - placement_lin[v])
    
    if total_lin <= B:
        print("YES")
        print(*(placement_lin[1:]))
        return
        
    # Conversely, check reversed linear placement (n, n-1, ..., 1).
    placement_lin_rev = [0] * (n + 1)
    for i in range(1, n + 1):
        placement_lin_rev[i] = n + 1 - i
    
    total_lin_rev = 0
    for u, v in pairs:
        total_lin_rev += abs(placement_lin_rev[u] - placement_lin_rev[v])
        
    if total_lin_rev <= B:
        print("YES")
        print(*(placement_lin_rev[1:]))
        return
    
    print("NO")

if __name__ == '__main__':
    solve()