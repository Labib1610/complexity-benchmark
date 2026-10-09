import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = True
        adj[v][u] = True
    
    # We use backtracking with constraint propagation.
    # Colors are 1, 2, 3.
    # We assign colors to vertices 1..n in order.
    # To find the lexicographically smallest valid coloring.
    
    color = [0] * (n + 1)
    
    # Precompute neighbors for faster access
    neighbors = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if adj[i][j]:
                neighbors[i].append(j)
    
    def is_possible():
        # Check if any uncolored vertex has all 3 colors used by colored neighbors
        for u in range(1, n + 1):
            if color[u] == 0:
                used = 0
                for v in neighbors[u]:
                    if color[v] != 0:
                        used |= (1 << color[v])
                if used == 0b1110: # colors 1, 2, 3 all used
                    return False
        return True

    def backtrack(idx):
        if idx > n:
            return True
        
        # Try colors 1, 2, 3 in order
        for c in range(1, 4):
            # Check if color c is valid for vertex idx
            ok = True
            for v in neighbors[idx]:
                if color[v] == c:
                    ok = False
                    break
            if not ok:
                continue
            
            color[idx] = c
            
            # Propagation: check for any immediate impossibility
            if is_possible():
                if backtrack(idx + 1):
                    return True
            
            color[idx] = 0
        
        return False

    if backtrack(1):
        print("YES")
        print(" ".join(map(str, color[1:n+1])))
    else:
        print("NO")

if __name__ == '__main__':
    solve()