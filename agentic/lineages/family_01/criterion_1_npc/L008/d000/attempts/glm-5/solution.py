import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
    
    # Check if graph is 3-colorable using backtracking with pruning
    # Since n <= 40, we use a recursive approach with bitmask representation
    
    color = [0] * (n + 1)  # 0: uncolored, 1, 2, 3: colors
    
    # Precompute neighbors for each node
    neighbors = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if adj[i] & (1 << (j - 1)):
                neighbors[i].append(j)
    
    # Order nodes by degree (heuristic for faster pruning)
    order = list(range(1, n + 1))
    order.sort(key=lambda x: -len(neighbors[x]))
    
    # Map from position in order to node number
    pos_to_node = order
    
    def dfs(pos):
        if pos == n:
            return True
        
        u = pos_to_node[pos]
        
        # Determine available colors
        used = 0
        for v in neighbors[u]:
            if color[v] != 0:
                used |= 1 << (color[v] - 1)
        
        for c in range(1, 4):
            if not (used & (1 << (c - 1))):
                color[u] = c
                if dfs(pos + 1):
                    return True
                color[u] = 0
        
        return False
    
    if dfs(0):
        print("YES")
        result = [0] * n
        for i in range(n):
            result[i] = color[pos_to_node[i]]
        print(' '.join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()