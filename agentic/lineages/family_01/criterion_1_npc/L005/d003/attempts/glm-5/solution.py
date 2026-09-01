import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * n for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u][v] = True
        adj[v][u] = True
    
    # We use backtracking with pruning.
    # p[i] stores the assigned value (1, 2, or 3) for emitter i.
    p = [0] * n
    
    # Check if assigning val to node u is valid with already assigned neighbors
    def is_valid(u, val):
        for v in range(u):
            if adj[u][v]:
                if (p[v] ^ val) == 0:
                    return False
        return True
    
    def backtrack(u):
        if u == n:
            return True
        
        for val in range(1, 4):
            if is_valid(u, val):
                p[u] = val
                if backtrack(u + 1):
                    return True
                p[u] = 0 # Backtrack, though not strictly necessary for correctness here
        return False

    if backtrack(0):
        print("YES")
        print(*(p))
    else:
        print("NO")

if __name__ == '__main__':
    solve()