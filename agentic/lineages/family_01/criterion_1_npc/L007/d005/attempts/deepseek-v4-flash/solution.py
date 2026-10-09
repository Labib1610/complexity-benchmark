import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # If no edges, any assignment works
    if m == 0:
        print("YES")
        print(' '.join(['1'] * n))
        return

    # Sort vertices by degree descending for better pruning
    degree = [len(adj[i]) for i in range(n)]
    order = sorted(range(n), key=lambda x: -degree[x])
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i

    # Build adjacency in new order
    adj_ordered = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            adj_ordered[pos[u]].append(pos[v])

    # Color assignment
    color = [-1] * n

    # Check if we can color vertex v with color c
    def is_safe(v, c):
        for nb in adj_ordered[v]:
            if color[nb] == c:
                return False
        return True

    # Backtracking with MRV heuristic
    def backtrack(idx):
        if idx == n:
            return True
        # Choose the next vertex (already ordered)
        v = idx  # since we process in order
        # Try colors 0,1,2
        for c in range(3):
            if is_safe(v, c):
                color[v] = c
                if backtrack(idx + 1):
                    return True
                color[v] = -1
        return False

    if backtrack(0):
        # Map back to original order
        res = [0] * n
        for i in range(n):
            res[i] = color[pos[i]] + 1  # +1 to get 1,2,3
        print("YES")
        print(' '.join(map(str, res)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()