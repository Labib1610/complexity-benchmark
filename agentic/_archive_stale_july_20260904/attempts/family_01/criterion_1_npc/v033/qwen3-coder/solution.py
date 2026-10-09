def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Try all 3^n assignments, starting from lexicographically smallest
    for assignment in product([1, 2, 3], repeat=n):
        # Check if this assignment is valid
        valid = True
        for u in range(1, n + 1):
            for v in adj[u]:
                if assignment[u - 1] == assignment[v - 1]:
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