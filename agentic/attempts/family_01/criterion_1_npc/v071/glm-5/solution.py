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
    
    # Check if graph is 3-colorable using backtracking with pruning
    # Since n <= 40, we need efficient pruning
    
    # Precompute neighbors for each vertex
    # We'll use a simple backtracking with constraint propagation
    
    # Order vertices by degree (largest first) for better pruning
    order = list(range(n))
    order.sort(key=lambda x: -len(adj[x]))
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i
    
    color = [0] * n  # 0 = uncolored, 1-3 = colors
    
    def is_safe(v, c):
        for neighbor in adj[v]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(idx):
        if idx == n:
            return True
        
        v = order[idx]
        for c in range(1, 4):
            if is_safe(v, c):
                color[v] = c
                if backtrack(idx + 1):
                    return True
                color[v] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()