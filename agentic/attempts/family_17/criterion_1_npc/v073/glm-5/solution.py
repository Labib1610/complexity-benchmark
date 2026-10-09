import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    crews = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        crews.append((a, b, c))
    
    n = 3 * q
    
    # Build adjacency list: for each specialist, list of crew indices containing them
    adj = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(crews):
        adj[a].append(i)
        adj[b].append(i)
        adj[c].append(i)
    
    # Track which crews are still available
    available = [True] * t
    
    # Track which specialists are still unassigned
    unassigned = [True] * (n + 1)
    
    # Count of unassigned specialists
    remaining = n
    
    # Result crews
    result = []
    
    # Use a stack for DFS-like processing
    stack = list(range(1, n + 1))
    
    while stack and remaining > 0:
        s = stack.pop()
        if not unassigned[s]:
            continue
        
        # Find an available crew containing s
        found = False
        for crew_idx in adj[s]:
            if available[crew_idx]:
                a, b, c = crews[crew_idx]
                if unassigned[a] and unassigned[b] and unassigned[c]:
                    # Use this crew
                    result.append((a, b, c))
                    available[crew_idx] = False
                    unassigned[a] = False
                    unassigned[b] = False
                    unassigned[c] = False
                    remaining -= 3
                    found = True
                    break
        
        if not found and unassigned[s]:
            # No valid crew found for this specialist
            print("NO")
            return
    
    if remaining == 0:
        print("YES")
        for crew in result:
            print(f"{crew[0]} {crew[1]} {crew[2]}")
    else:
        print("NO")

solve()