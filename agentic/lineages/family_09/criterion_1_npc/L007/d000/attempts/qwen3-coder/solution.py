from itertools import combinations

def solve():
    n, m, k = map(int, input().split())
    
    # Create adjacency list to represent conflicts
    conflicts = set()
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts.add((u, v))
        conflicts.add((v, u))
        adj[u].append(v)
        adj[v].append(u)
    
    # Check all combinations of k experiments
    for combo in combinations(range(1, n + 1), k):
        valid = True
        # Check if any two experiments in the combination conflict
        for i in range(k):
            for j in range(i + 1, k):
                if (combo[i], combo[j]) in conflicts:
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            print("YES")
            print(*combo)
            return
    
    print("NO")

solve()