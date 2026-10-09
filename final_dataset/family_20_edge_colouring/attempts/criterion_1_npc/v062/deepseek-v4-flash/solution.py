import sys
sys.setrecursionlimit(10000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    color = [-1] * m
    
    # Check if graph is 3-regular
    for i in range(n):
        if len(adj[i]) != 3:
            print("NO")
            return
    
    # Try to color edges with backtracking
    # We'll use a simple backtracking with MRV heuristic
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
        # Find uncolored edge with fewest options
        best = -1
        best_options = None
        for i in range(m):
            if color[i] == -1:
                u, v = edges[i]
                used = set()
                for _, eid in adj[u]:
                    if color[eid] != -1:
                        used.add(color[eid])
                for _, eid in adj[v]:
                    if color[eid] != -1:
                        used.add(color[eid])
                options = [c for c in (1,2,3) if c not in used]
                if best == -1 or len(options) < len(best_options):
                    best = i
                    best_options = options
                    if len(options) == 0:
                        return False
                    if len(options) == 1:
                        break
        if best == -1:
            return True
        for c in best_options:
            color[best] = c
            if backtrack(edge_idx + 1):
                return True
            color[best] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(color[i]) for i in range(m)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()