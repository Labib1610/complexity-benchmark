import sys
sys.setrecursionlimit(100000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to 2-color the graph using shifts 1 and 2
    color = [-1] * n
    is_bipartite = True
    components = []
    
    for i in range(n):
        if color[i] == -1:
            comp = []
            stack = [i]
            color[i] = 0
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
            components.append(comp)
    
    if is_bipartite:
        print("YES")
        result = [1 if color[i] == 0 else 2 for i in range(n)]
        print(' '.join(map(str, result)))
        return
    
    # Check if 3-coloring is possible using backtracking
    assignment = [0] * n
    
    # Order vertices by degree for better pruning
    order = list(range(n))
    order.sort(key=lambda x: len(adj[x]), reverse=True)
    
    def backtrack(idx):
        if idx == n:
            return True
        u = order[idx]
        used = 0
        for v in adj[u]:
            if assignment[v] != 0:
                used |= (1 << (assignment[v] - 1))
        for c in range(1, 4):
            if not (used & (1 << (c - 1))):
                assignment[u] = c
                if backtrack(idx + 1):
                    return True
                assignment[u] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

solve()