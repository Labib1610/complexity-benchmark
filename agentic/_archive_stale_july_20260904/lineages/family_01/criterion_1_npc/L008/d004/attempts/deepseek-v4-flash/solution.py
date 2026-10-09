import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    colors = [0] * n
    # Precompute adjacency bitmasks
    adj_mask = [0] * n
    for i in range(n):
        mask = 0
        for j in adj[i]:
            mask |= (1 << j)
        adj_mask[i] = mask
    
    # Sort vertices by degree (largest first) for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    
    def backtrack(idx):
        if idx == n:
            return True
        v = order[idx]
        used = 0
        for u in adj[v]:
            if colors[u]:
                used |= (1 << (colors[u] - 1))
        for c in range(1, 4):
            if not (used & (1 << (c - 1))):
                colors[v] = c
                if backtrack(idx + 1):
                    return True
                colors[v] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(colors[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()