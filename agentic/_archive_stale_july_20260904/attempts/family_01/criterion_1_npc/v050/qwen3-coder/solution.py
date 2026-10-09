def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    conflicts = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        conflicts.append((u, v))
        index += 2
    
    # We need to check all combinations in lexicographical order (which product gives us)
    # Since we want the lex smallest valid assignment, we generate in order:
    for config in product([1, 2, 3], repeat=n):
        valid = True
        for u, v in conflicts:
            if config[u] == config[v]:
                valid = False
                break
        if valid:
            print("YES")
            print(' '.join(map(str, config)))
            return
            
    print("NO")

solve()