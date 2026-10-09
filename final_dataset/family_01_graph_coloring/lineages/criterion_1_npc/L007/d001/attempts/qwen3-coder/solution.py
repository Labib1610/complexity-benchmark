def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = [set() for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].add(v)
        adj[v].add(u)
        index += 2
    
    # Try all 3^n combinations
    for combo in product([1, 2, 3], repeat=n):
        valid = True
        for i in range(1, n + 1):
            for neighbor in adj[i]:
                if combo[i-1] == combo[neighbor-1]:
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            print("YES")
            print(" ".join(map(str, combo)))
            return
    
    print("NO")

solve()