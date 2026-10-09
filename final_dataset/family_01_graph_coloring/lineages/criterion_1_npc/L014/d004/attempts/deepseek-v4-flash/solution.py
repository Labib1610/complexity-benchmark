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
    
    colors = [0] * n
    # available colors for each node: 1,2,3
    
    # Sort vertices by degree descending for better backtracking order
    order = sorted(range(n), key=lambda x: len(adj[x]), reverse=True)
    
    # Simple backtracking with MRV heuristic
    
    def dfs(pos):
        if pos == n:
            return True
        v = order[pos]
        # Try colors 1,2,3
        for c in (1,2,3):
            ok = True
            for nb in adj[v]:
                if colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[v] = c
                if dfs(pos + 1):
                    return True
                colors[v] = 0
        return False
    
    if dfs(0):
        print("YES")
        print(" ".join(str(colors[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()