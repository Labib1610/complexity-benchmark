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
    
    colors = [0] * n  # 0 = uncolored, 1,2,3 = voltage levels
    
    # Precompute available colors for each vertex
    def available_colors(v):
        used = set()
        for nb in adj[v]:
            if colors[nb] != 0:
                used.add(colors[nb])
        return [c for c in (1, 2, 3) if c not in used]
    
    # MRV heuristic: pick uncolored vertex with fewest available colors
    def select_vertex():
        best_v = -1
        best_len = 4
        for v in range(n):
            if colors[v] == 0:
                avail = available_colors(v)
                if len(avail) < best_len:
                    best_len = len(avail)
                    best_v = v
                    if best_len == 0:
                        break
        return best_v
    
    def backtrack():
        v = select_vertex()
        if v == -1:
            return True
        for c in available_colors(v):
            colors[v] = c
            if backtrack():
                return True
            colors[v] = 0
        return False
    
    if backtrack():
        print("YES")
        print(" ".join(str(c) for c in colors))
    else:
        print("NO")

if __name__ == "__main__":
    solve()