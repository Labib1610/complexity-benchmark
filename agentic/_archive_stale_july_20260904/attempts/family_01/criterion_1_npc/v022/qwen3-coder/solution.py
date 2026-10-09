def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-indexed
        v = int(data[idx+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    # Try all 3^n combinations, starting from lexicographically smallest
    for assignment in product([1, 2, 3], repeat=n):
        valid = True
        for i in range(n):
            for neighbor in adj[i]:
                if assignment[i] == assignment[neighbor]:
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