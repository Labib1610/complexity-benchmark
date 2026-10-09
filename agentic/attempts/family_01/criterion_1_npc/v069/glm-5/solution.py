import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)
    
    # Check if graph is 3-colorable
    # Using backtracking with pruning
    
    color = [0] * n
    
    # Order vertices by degree (descending) for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    
    # Precompute adjacency list for ordered vertices
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        for j in adj[i]:
            adj_list[i].append(j)
    
    def is_safe(node, c):
        for neighbor in adj_list[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(idx):
        if idx == n:
            return True
        
        node = order[idx]
        for c in range(1, 4):
            if is_safe(node, c):
                color[node] = c
                if backtrack(idx + 1):
                    return True
                color[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()