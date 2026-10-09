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
    
    colors = [0] * n  # 0 = uncolored, 1,2,3 = colors
    
    # Sort vertices by degree for better pruning
    order = sorted(range(n), key=lambda x: len(adj[x]), reverse=True)
    
    def backtrack(idx):
        if idx == n:
            return True
        v = order[idx]
        used = [False] * 4
        for nb in adj[v]:
            if colors[nb] != 0:
                used[colors[nb]] = True
        for c in range(1, 4):
            if not used[c]:
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