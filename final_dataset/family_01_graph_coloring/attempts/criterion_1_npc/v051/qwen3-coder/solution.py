def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Create adjacency list representation of the graph
    adj = [[] for _ in range(n+1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    # Try all possible assignments of instruments to booms
    # Each instrument can be assigned to boom 1, 2, or 3
    for assignment in product([1, 2, 3], repeat=n):
        # Check if this assignment is valid
        valid = True
        for u in range(1, n+1):
            for v in adj[u]:
                # If two interfering instruments are on the same boom
                if assignment[u-1] == assignment[v-1]:
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

solve()