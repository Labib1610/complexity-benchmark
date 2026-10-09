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
    
    color = [0] * n  # 0 = unassigned, 1,2,3 = shifts
    
    # Sort vertices by degree (largest first) for better pruning
    order = sorted(range(n), key=lambda x: len(adj[x]), reverse=True)
    pos = [0] * n
    for idx, v in enumerate(order):
        pos[v] = idx
    
    # Build adjacency in order indices
    adj_ordered = [[] for _ in range(n)]
    for v in range(n):
        for u in adj[v]:
            adj_ordered[pos[v]].append(pos[u])
    
    def backtrack(idx):
        if idx == n:
            return True
        v = order[idx]
        used = [False] * 4
        for u in adj[v]:
            if color[u] != 0:
                used[color[u]] = True
        for c in range(1, 4):
            if not used[c]:
                color[v] = c
                if backtrack(idx + 1):
                    return True
                color[v] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()