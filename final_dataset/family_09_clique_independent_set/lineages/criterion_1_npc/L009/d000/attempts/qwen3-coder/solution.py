from itertools import combinations

def solve():
    n, m, k = map(int, input().split())
    
    # Create adjacency list to represent conflicts
    conflicts = set()
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts.add((u, v))
        conflicts.add((v, u))
    
    # Generate all possible combinations of k artifacts
    artifacts = list(range(1, n + 1))
    
    # Check each combination
    for combo in combinations(artifacts, k):
        # Check if this combination is stable
        valid = True
        for i in range(k):
            for j in range(i + 1, k):
                if (combo[i], combo[j]) in conflicts:
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