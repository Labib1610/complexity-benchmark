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

    color = [0] * n

    # Precompute possible colors for each vertex based on neighbors already colored
    def backtrack(idx):
        if idx == n:
            return True
        # Choose vertex with most constraints (MRV heuristic)
        best = -1
        best_options = None
        for i in range(n):
            if color[i] == 0:
                used = set()
                for nb in adj[i]:
                    if color[nb] != 0:
                        used.add(color[nb])
                options = [c for c in (1,2,3) if c not in used]
                if best == -1 or len(options) < len(best_options):
                    best = i
                    best_options = options
                    if len(options) == 0:
                        break
        if best == -1:
            return True
        if not best_options:
            return False
        # Try colors in order
        for c in best_options:
            color[best] = c
            if backtrack(idx + 1):
                return True
            color[best] = 0
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color))))
    else:
        print("NO")

if __name__ == "__main__":
    solve()