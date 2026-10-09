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
    
    colors = [-1] * n
    
    # Check if we can color with backtracking
    def backtrack(idx):
        if idx == n:
            return True
        # Choose uncolored vertex with most colored neighbors (DSATUR)
        best = -1
        best_deg = -1
        for v in range(n):
            if colors[v] == -1:
                # count distinct colors among neighbors
                neigh_colors = set()
                for nb in adj[v]:
                    if colors[nb] != -1:
                        neigh_colors.add(colors[nb])
                sat_deg = len(neigh_colors)
                if sat_deg > best_deg or (sat_deg == best_deg and len(adj[v]) > len(adj[best])):
                    best_deg = sat_deg
                    best = v
        v = best
        # Try colors 1,2,3
        for c in range(1, 4):
            ok = True
            for nb in adj[v]:
                if colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[v] = c
                if backtrack(idx + 1):
                    return True
                colors[v] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(colors[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()