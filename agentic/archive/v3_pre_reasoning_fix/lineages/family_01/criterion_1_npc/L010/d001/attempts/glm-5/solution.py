python
def solve():
    import sys
    sys.setrecursionlimit(10000)
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    assignment = [0] * n
    
    def backtrack(node):
        if node == n:
            return True
        for tier in [1, 2, 3]:
            valid = True
            for neighbor in adj[node]:
                if assignment[neighbor] == tier:
                    valid = False
                    break
            if valid:
                assignment[node] = tier
                if backtrack(node + 1):
                    return True
        assignment[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()
```