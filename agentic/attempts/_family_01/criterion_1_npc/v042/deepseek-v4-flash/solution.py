[code]
import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[False] * n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u][v] = adj[v][u] = True

    # Try all 3^n assignments? n <= 40, too large.
    # Use backtracking with pruning: assign each vertex one of 3 colors,
    # but we can use symmetry: fix vertex 0 to color 0, and vertex 1 to color 0 or 1.
    # Actually n <= 40, 3^40 is too big. Need smarter.
    # This is graph 3-coloring. n=40, m up to 780. Use backtracking with DSATUR or simple pruning.
    # Since 3 colors, we can do recursive backtracking with ordering by degree.
    # Worst case might be hard, but constraints small enough with pruning.

    color = [-1] * n
    # order vertices by degree descending for better pruning
    deg = [sum(adj[i]) for i in range(n)]
    order = sorted(range(n), key=lambda x: -deg[x])

    # Precompute adjacency list
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if adj[i][j]:
                adj_list[i].append(j)

    # Try to color
    def backtrack(idx):
        if idx == n:
            return True
        v = order[idx]
        # Try colors 0,1,2
        for c in range(3):
            ok = True
            for nb in adj_list[v]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[v] = c
                if backtrack(idx + 1):
                    return True
                color[v] = -1
        return False

    # Symmetry breaking: fix first vertex to color 0
    v0 = order[0]
    color[v0] = 0
    if not backtrack(1):
        print("NO")
        return

    # Output
    print("YES")
    # color values 0,1,2 -> rings 1,2,3
    print(' '.join(str(color[i] + 1) for i in range(n)))

if __name__ == "__main__":
    solve()