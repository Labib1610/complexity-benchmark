import sys

def solve():
    data = sys.stdin.read().strip().split()
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
    
    # Check if graph is bipartite using BFS
    color = [-1] * n
    is_bipartite = True
    q = []
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q.append(i)
            while q:
                u = q.pop(0)
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
    
    if not is_bipartite:
        print("NO")
        return
    
    # Graph is bipartite, find lexicographically smallest valid assignment
    # Using backtracking with pruning
    assignment = [0] * n
    
    def get_available_values(node):
        """Get available values for a node based on assigned neighbors"""
        used = set()
        for neighbor in adj[node]:
            if assignment[neighbor] != 0:
                used.add(assignment[neighbor])
        return [v for v in [1, 2, 3] if v not in used]
    
    def backtrack(idx):
        if idx == n:
            return True
        
        for val in get_available_values(idx):
            assignment[idx] = val
            if backtrack(idx + 1):
                return True
            assignment[idx] = 0
        
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

solve()