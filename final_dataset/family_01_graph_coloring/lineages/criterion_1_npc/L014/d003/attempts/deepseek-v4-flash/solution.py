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
    
    # MRV heuristic: pick uncolored vertex with most colored neighbors
    def select_uncolored_vertex():
        best = -1
        best_degree = -1
        for i in range(n):
            if colors[i] == 0:
                # count colored neighbors
                cnt = sum(1 for nb in adj[i] if colors[nb] != 0)
                if cnt > best_degree:
                    best_degree = cnt
                    best = i
        return best
    
    def is_safe(v, c):
        for nb in adj[v]:
            if colors[nb] == c:
                return False
        return True
    
    def backtrack():
        v = select_uncolored_vertex()
        if v == -1:
            return True  # all colored
        for c in (1, 2, 3):
            if is_safe(v, c):
                colors[v] = c
                if backtrack():
                    return True
                colors[v] = 0
        return False
    
    if backtrack():
        print("YES")
        print(" ".join(str(colors[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()