import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    # adjacency bitmask
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Try to find 3-coloring
    color = [-1] * n
    
    # We'll use backtracking with MRV heuristic
    def is_safe(v, c):
        # check all neighbors
        for u in range(n):
            if (adj[v] >> u) & 1:
                if color[u] == c:
                    return False
        return True
    
    # Sort vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: bin(adj[x]).count('1'), reverse=True)
    
    def backtrack(idx):
        if idx == n:
            return True
        v = order[idx]
        for c in range(3):
            if is_safe(v, c):
                color[v] = c
                if backtrack(idx + 1):
                    return True
                color[v] = -1
        return False
    
    if not backtrack(0):
        print("NO")
        return
    
    print("YES")
    print(' '.join(str(c + 1) for c in color))

if __name__ == "__main__":
    solve()