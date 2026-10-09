import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    color = [-1] * n
    # Try to color with 3 colors using backtracking
    # We'll use DSATUR ordering: pick uncolored vertex with max saturation
    def backtrack():
        # Find uncolored vertex with max saturation
        best = -1
        best_sat = -1
        best_deg = -1
        for v in range(n):
            if color[v] == -1:
                sat = 0
                mask = 0
                for u in range(n):
                    if (adj[v] >> u) & 1 and color[u] != -1:
                        mask |= 1 << color[u]
                sat = bin(mask).count("1")
                deg = bin(adj[v]).count("1")
                if sat > best_sat or (sat == best_sat and deg > best_deg):
                    best_sat = sat
                    best_deg = deg
                    best = v
        if best == -1:
            return True
        v = best
        # Try colors 0,1,2
        forbidden = 0
        for u in range(n):
            if (adj[v] >> u) & 1 and color[u] != -1:
                forbidden |= 1 << color[u]
        for c in range(3):
            if not (forbidden >> c) & 1:
                color[v] = c
                if backtrack():
                    return True
                color[v] = -1
        return False

    if backtrack():
        print("YES")
        print(" ".join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()