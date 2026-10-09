import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().split()
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
    
    # Precompute valid pairs
    # valid[a][b] is True if pair (a, b) is stable
    valid = [[False] * 4 for _ in range(4)]
    for u in range(1, 4):
        for v in range(1, 4):
            if u ** 3 + v ** 3 > (u + v) * u * v:
                valid[u][v] = True
    
    color = [0] * n
    
    def dfs(u):
        for v in adj[u]:
            if color[v] == 0:
                color[v] = 3 - color[u]
                if not dfs(v):
                    return False
            elif color[v] == color[u]:
                return False
        return True
    
    # Check if graph is bipartite
    is_bipartite = True
    for i in range(n):
        if color[i] == 0:
            color[i] = 1
            if not dfs(i):
                is_bipartite = False
                break
    
    if is_bipartite:
        # Bipartite: assign 1 to part 1, 2 to part 2
        # This is lexicographically smallest for bipartite graphs
        res = [0] * n
        for i in range(n):
            res[i] = color[i]
        print("YES")
        print(" ".join(map(str, res)))
        return
    
    # Not bipartite: must use 3
    # Check if all edges can be made stable using values in {1, 2, 3}
    # For an edge to be stable, it cannot be (1, 1) or (2, 2)
    # So we need to 2-color the graph using colors from {1, 2, 3}
    # where adjacent vertices get different colors from {1, 2}
    # This is possible iff each connected component is bipartite
    
    comp = [-1] * n
    part = [-1] * n
    comp_id = 0
    possible = True
    
    for start in range(n):
        if comp[start] != -1:
            continue
        # BFS to check if component is bipartite
        queue = [start]
        comp[start] = comp_id
        part[start] = 0
        bip = True
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v in adj[u]:
                if comp[v] == -1:
                    comp[v] = comp_id
                    part[v] = 1 - part[u]
                    queue.append(v)
                elif part[v] == part[u]:
                    bip = False
        if not bip:
            possible = False
            break
        comp_id += 1
    
    if not possible:
        print("NO")
        return
    
    # Construct lexicographically smallest assignment
    # For each component: part 0 gets 1, part 1 gets 2
    res = [0] * n
    for i in range(n):
        res[i] = part[i] + 1
    
    print("YES")
    print(" ".join(map(str, res)))

solve()