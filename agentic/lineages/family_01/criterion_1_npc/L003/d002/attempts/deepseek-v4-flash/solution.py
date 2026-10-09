import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m = int(input_data[0]), int(input_data[1])
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    colors = [0] * n  # 0 = uncolored, 1,2,3 = colors
    
    # Sort vertices by degree for better pruning
    order = sorted(range(n), key=lambda x: len(adj[x]), reverse=True)
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i
    
    # Build adjacency in new order
    adj_ordered = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            adj_ordered[pos[u]].append(pos[v])
    
    def backtrack(i):
        if i == n:
            return True
        v = order[i]
        used = [False] * 4
        for nb in adj_ordered[i]:
            if colors[nb] != 0:
                used[colors[nb]] = True
        for c in (1, 2, 3):
            if not used[c]:
                colors[i] = c
                if backtrack(i + 1):
                    return True
                colors[i] = 0
        return False
    
    if backtrack(0):
        # Map back to original order
        result = [0] * n
        for i, v in enumerate(order):
            result[v] = colors[i]
        print("YES")
        print(" ".join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()