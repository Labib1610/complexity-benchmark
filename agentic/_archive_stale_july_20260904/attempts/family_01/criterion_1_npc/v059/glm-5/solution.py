import sys

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
    
    # Try to color with 2 colors first (greedy, lexicographically smallest)
    color = [0] * n
    is_bipartite = True
    
    for start in range(n):
        if color[start] == 0:
            color[start] = 1
            queue = [start]
            for u in queue:
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
    
    if is_bipartite:
        print("YES")
        print(' '.join(map(str, color)))
        return
    
    # Try 3-coloring with backtracking
    assignment = [0] * n
    
    # Precompute neighbors for faster access
    # Order: try colors 1, 2, 3 for each vertex
    
    def backtrack(idx):
        if idx == n:
            return True
        for c in range(1, 4):
            valid = True
            for v in adj[idx]:
                if v < idx and assignment[v] == c:
                    valid = False
                    break
            if valid:
                assignment[idx] = c
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